from re import L
from typing import Iterator, List
import heapq
#from kth_largest_in_array import find_kth_largest

from test_framework import generic_test


def find_kth_largest_unknown_length(stream: Iterator[int], k: int) -> int:
    candidates = []
    for i in stream:
        candidates.append(i)
        if len(candidates) >= 2 * k - 1:
            find_kth_largest(k, candidates)
            del candidates[:k-1]
    return find_kth_largest(k, candidates)

def find_kth_largest(k: int, A: List[int]):
    if not A or k < 1 or k > len(A):
        raise ValueError("k must be within the lenght of A")

    target_index = len(A) - k

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = A[pivot_index]
        store_index = left
        A[pivot_index], A[right] = A[right], A[pivot_index]
        for i in range(left, right):
            if A[i] < pivot_value:
                A[i], A[store_index] = A[store_index], A[i]
                store_index += 1
        A[store_index], A[right] = A[right], A[store_index]
        return store_index
            

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_index = (left + right) // 2
        new_pivot_index = partition(left, right, pivot_index)
        if new_pivot_index == target_index:
            return A[new_pivot_index]
        if new_pivot_index < target_index:
            left = new_pivot_index + 1
        else:
            right = new_pivot_index - 1
    return A[new_pivot_index]


# Pythonic solution that uses library method but costs O(nlogk) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


def find_kth_largest_unknown_length_wrapper(stream, k):
    return find_kth_largest_unknown_length(iter(stream), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'kth_largest_element_in_long_array.py',
            'kth_largest_element_in_long_array.tsv',
            find_kth_largest_unknown_length_wrapper))
