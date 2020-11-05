#!/bin/bash

if [[ $# != 2 ]]; then
  echo "Usage: $0 <path/to/directory/with/tests> <path/to/executable> " >&2
  exit 1
fi

tests=$(realpath "$1")
executable=$(realpath "$2")
threshold=${3:-1}

if ! [[ -d "$tests" ]]; then
  echo "Given directory with tests does not exist."
  exit 1
fi

if ! [[ -f "$executable" ]]; then
  echo "Given executable does not exist."
  exit 1
fi

total=0
correct=0
leaked=0

function traverse_folder() {
  folder="$1"
  shopt -s nullglob
  for test_file in "$folder"/*.in; do
    randfloat=$(printf '0%s\n' $(echo "scale=8; $RANDOM/32768" | bc ))
    if (( $(echo "$randfloat < $threshold" |bc -l) )); then
      run_test "${test_file}"
    fi
  done

  shopt -s nullglob
  for dir in "$folder"/*/; do
    echo "${dir}"
    traverse_folder "$(realpath "${dir}")"
  done
}

RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'

function run_test() {
  input_file="$1"
  output_file=${input_file//.in/.out}
  error_file=${input_file//.in/.err}

  ((total++))
  echo -e "\e[1mTest ${input_file} \e[0m"

  cat "$input_file" | ${executable}  1>"$temp_out" 2>"$temp_err"

    if cmp -s "$output_file" "$temp_out" ; then
        echo -ne "${GREEN}stdout ok${NOCOLOR}, "
	
	if [[ -f "$error_file" ]]; then
		if cmp -s "$error_file" "$temp_err" ; then
		    echo -ne "${GREEN}stderr ok${NOCOLOR}\n"
		    ((correct++))
		else
		    echo -ne "${RED}stderr nieprawidlowe${NOCOLOR}\n"
		    diff -d "$error_file" "$temp_err"
		fi
	else
		printf "\n"
		((correct++))
	fi

    else
        echo -ne "${RED}stdout nieprawidlowe${NOCOLOR}\n"
        diff -d "$output_file" "$temp_out"
    fi
  }

temp_out=$(mktemp)
temp_err=$(mktemp)
trap 'rm -f "$temp_out"' INT TERM HUP EXIT

traverse_folder "$tests"

echo "total: ${total}, correct ${correct}"

