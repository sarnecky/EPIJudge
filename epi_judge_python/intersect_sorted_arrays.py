import re
from typing import List

from test_framework import generic_test
import bisect

# O(nm)
def intersect_two_sorted_arrays_brute(A: List[int], B: List[int]) -> List[int]:
    return [a for i,a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]
    
# O(nlogm)
def intersect_two_sorted_arrays_binary_search(A: List[int], B: List[int]) -> List[int]:
    def is_present(k):
       i = bisect.bisect_left(B, k) 
       return i < len(B) and B[i] == k

    return [a for i,a in enumerate(A) if (i == 0 or a != A[i -1]) and is_present(a)]

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    a_index, b_index, intersection_result = 0, 0, []
    while a_index < len(A) and b_index < len(B):
        if A[a_index] == B[b_index]:
            if a_index == 0 or A[a_index] != A[a_index - 1]:
                intersection_result.append(A[a_index])
            a_index, b_index = a_index + 1, b_index + 1
        elif A[a_index] < B[b_index]:
            a_index+=1
        else:
            b_index+=1
    return intersection_result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
