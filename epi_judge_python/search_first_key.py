from typing import List

from test_framework import generic_test

# O(log n) time, O(1) space
def search_first_of_k(A: List[int], k: int) -> int:
    result, left, right = -1, 0, len(A) - 1
    while left <= right:
        middle = (right + left)//2
        if A[middle] == k:
            result = middle
            right = middle - 1
        elif A[middle] < k:
            left = middle + 1
        else :
            right = middle - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
