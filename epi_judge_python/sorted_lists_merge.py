from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# time conplexity O(n + m)
# space complexity O(1)

# two pointers approach - use two pointers to traverse both sorted lists simultaneously
# example:
# dummy_head is for simplify merge process. It has keep state of merged collection
# current is property that keeps current node
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    current_node = ListNode();
    first_node = current_node
    while L1 and L2:
        if L1.data <= L2.data:
            current_node.next = L1
            L1 = L1.next
        else:
            current_node.next = L2
            L2 = L2.next
        current_node = current_node.next
    
    current_node.next = L1 or L2
    return first_node.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))


