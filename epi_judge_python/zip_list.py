from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_list(head: ListNode) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L
    
    fast = slow = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    first_half_head = L
    second_half_head = slow.next
    slow.next = None  # Break the connection between halves

    second_half_head = reverse_list(second_half_head)
    first_half_iter, second_half_iter = first_half_head, second_half_head
    while second_half_iter:
        # Save the next nodes before modifying pointers
        temp_first = first_half_iter.next
        temp_second = second_half_iter.next
        
        # Insert second_half_iter after first_half_iter
        first_half_iter.next = second_half_iter
        second_half_iter.next = temp_first
        
        # Move to next nodes
        first_half_iter = temp_first
        second_half_iter = temp_second
    return first_half_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
