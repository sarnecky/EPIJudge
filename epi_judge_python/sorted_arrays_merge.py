from typing import List
from heapq import heappush, heappop

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[tuple[int, int]] = []
    sorted_arrays_iterators = [iter(arr) for arr in sorted_arrays]
    for i, arr in enumerate(sorted_arrays_iterators):
        first_element = next(arr, None)
        if first_element is not None:
            heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_element, smallest_element_array_idx = heappop(min_heap)
        result.append(smallest_element)
        next_element = next(sorted_arrays_iterators[smallest_element_array_idx], None)
        if next_element is not None:
            heappush(min_heap, (next_element, smallest_element_array_idx))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
