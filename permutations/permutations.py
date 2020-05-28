from typing import List
import random
from itertools import permutations


def random_permutation(data: List) -> List:
    """Return random permutation of elements in data.
    
    Algorithm based on Fisher–Yates shuffle.
    """

    permutation = data.copy()
    n = len(data)

    for i in range(n):
        number = random.randint(i, n-1)
        permutation[i], permutation[number] = permutation[number], permutation[i]

    return permutation

def my_random_permutation(data: List) -> List:
    """Return random permutation of elements in data.
    
    My attempt to create random permutation.
    """

    items = data.copy()
    permutation = []

    for i in range(len(data)):
        choice = random.randint(0, len(items) - 1)
        permutation.append(items[choice])
        items.pop(choice)
    
    return permutation

def permutations(data: List) -> List[List]:
    """Return all permutations of elements in data."""

    if len(data) <= 1:
        return [data]
    
    result = []

    for i in range(len(data)):
        permutation = [data[i]]

        for rest_of_permutation in permutations(data[:i] + data[i+1:]):
            result.append(permutation + rest_of_permutation)
    
    return result
