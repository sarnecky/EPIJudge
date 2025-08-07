from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# important to keep sublist_head
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # sublist_head -> pointer to head before sublist, sublist_head.next -> first element of the sublist
    # working_pointer -> element which will be moved forward
    # node to be extracted -> element which will be moved backward
    working_pointer = sublist_head.next
    for _ in range(finish - start):
        node_to_be_extaxcted = working_pointer.next
        working_pointer.next = node_to_be_extaxcted.next
        node_to_be_extaxcted.next = sublist_head.next
        sublist_head.next = node_to_be_extaxcted
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
