from typing import List, Tuple
import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    
    max_heap: List[Tuple[int, int]] = []
    max_heap.append((-A[0], 0))
    result = []

    for _ in range(k):
        candidate_index = max_heap[0][1]
        result.append(-heapq.heappop(max_heap)[0])

        left_child_index = 2 * candidate_index + 1
        if left_child_index < len(A):
            heapq.heappush(max_heap, (-A[left_child_index], left_child_index))

        right_child_index = 2 * candidate_index + 2
        if right_child_index < len(A):
            heapq.heappush(max_heap, (-A[right_child_index], right_child_index))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
