from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None
    
    # computes lenght of L, and tail
    n, tail = 1, L
    while tail.next:
        tail = tail.next
        n += 1

    k = k % n
    if k == 0:
        return L
    
    tail.next = L
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        new_tail = new_tail.next
        steps_to_new_head -=1
    
    new_head = new_tail.next
    new_tail.next = None
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
