from typing import List

from sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_subarrays = []
    increasing, decreasing = range(2)
    current_array_type = increasing
    start_ind = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or
          (A[i - 1] < A[i] and current_array_type == decreasing) or
          (A[i - 1] >= A[i] and current_array_type == increasing)):
            sorted_subarrays.append(A[start_ind:i] if current_array_type == increasing else A[i - 1: start_ind - 1: -1])
            start_ind = i
            current_array_type = (decreasing if current_array_type == increasing else increasing)

    return merge_sorted_arrays(sorted_subarrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
