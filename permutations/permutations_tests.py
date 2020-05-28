import itertools
import time
from typing import List

import permutations


def test(data: List, debug: bool=False):
    """Compare results of creating all permutations of given data
    by itertools.permutations and permutations.permutations"""

    if debug:
        print('-'*50)
        print(f'data: {data}')
        print('itertools.permutations start.')
        start = time.time()

    expected_result = list(itertools.permutations(data))

    if debug:
        stop = time.time()
        print(f'itertools.permutations time: {stop-start}')
        print()
        print('permutations.permutations start.')
        start = time.time()

    result = permutations.permutations(data)

    if debug:
        stop = time.time()
        print(f'permutations.permutations time: {stop-start}')

    expected_result = sorted(list(expected_result))
    result = sorted([tuple(p) for p in result])

    assert(result == expected_result)

    if debug:
        print('OK')
        print('-'*50)

    
if __name__ == "__main__":
    n = 10

    for i in range(n):
        test_data = [k for k in range(i)]

        test(test_data, debug=True)

    test(['aa', 'bb', 'cc'], debug=True)


