from typing import List

from test_framework import generic_test


def find_first_missing_positive(A: List[int]) -> int:
    i = 0
    while i < len(A):
        if 1 <= A[i] <= len(A) and A[i] != A[A[i] -1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        else:
            i += 1

    for i, e in enumerate(A):
        if e != i + 1:
            return i + 1
    return len(A) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('first_missing_positive_entry.py',
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
