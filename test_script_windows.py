import subprocess
import os
import time
import difflib

current_dir = os.getcwd()
tests_dir = os.path.join(current_dir, 'tests')
out_dir = os.path.join(current_dir, 'out')
exe_file = os.path.join(current_dir, ".exe")


def run_test(test):
	print('*' * 50)
	print(f'Running test {test}')

	before = time.time()
	subprocess.call(
		f'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe ' + 
		f'type {tests_dir}\\{test}.in | {exe_file}' +
		f'> {out_dir}\\{test}.out', shell=True)
	after = time.time()


	elapsed = round(after - before, 2)
	print(f'Time elapsed: {elapsed}s')

	correct_out = os.path.join(tests_dir, f'{test}.out')
	current_out = os.path.join(out_dir, f'{test}.out')
	
	# Get differences between current and correct output files.
	with open(current_out) as current_out_file:
		with open(correct_out) as correct_out_file:
			diff = difflib.unified_diff(
				current_out_file.readlines(),
				correct_out_file.readlines(),
				fromfile='current',
				tofile='correct'
			)
			diff_line_count = 0
			for line in diff:
				diff_line_count += 1
				print(line)

	return diff_line_count == 0


def run_tests(tests):
	count = 0
	correct = 0
	for test in tests:
		count += 1
		
		if run_test(test):
			correct += 1
			print('OK')
		else:
			print('INCORRECT')

	print(f'Correct {correct} of {count}')


# Get all .in files
tests = [test[:-3] for test in os.listdir(tests_dir) if test[-3] == '.']

run_tests(tests)
