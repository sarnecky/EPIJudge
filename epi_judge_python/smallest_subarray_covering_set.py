import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    class DoublyLinkedListNode:
        def __init__(self, data=None) -> None:
            self.data = data
            self.next = None
            self.prev = None

    class LinkedList:
        def __init__(self) -> None:
            self.head = None
            self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def insert_after(self, value):
            node  = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -=1
    
    loc = LinkedList()
    d = { s : None for s in keywords }
    result = Subarray(-1, -1)
    for idx, s in enumerate(paragraph):
        if s in d: # if s exists in keywords
            it = d[s]
            if it is not None:
                loc.remove(it)

            loc.insert_after(idx)
            d[s] = loc.tail

        if len(loc) == len(keywords):
            if result == (-1, -1) or result[1] - result[0] > idx - loc.head.data:
                result = Subarray(loc.head.data, idx)

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
