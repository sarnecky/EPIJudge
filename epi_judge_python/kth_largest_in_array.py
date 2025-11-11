from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # Quickselect: find element with index (len(A) - k) in sorted order
    if not A or k < 1 or k > len(A):
        raise ValueError("k must be within the length of A")

    target_index = len(A) - k

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = A[pivot_index]
        A[pivot_index], A[right] = A[right], A[pivot_index]
        store_index = left
        for i in range(left, right):
            if A[i] < pivot_value:
                A[store_index], A[i] = A[i], A[store_index]
                store_index += 1
        A[right], A[store_index] = A[store_index], A[right]
        return store_index

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_index = (left + right) // 2
        new_index = partition(left, right, pivot_index)
        if new_index == target_index:
            return A[new_index]
        if new_index < target_index:
            left = new_index + 1
        else:
            right = new_index - 1
    # Fallback, though loop should always return
    return A[target_index]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
