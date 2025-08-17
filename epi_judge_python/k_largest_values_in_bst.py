from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def find_largest_helper(tree: BstNode): # revese in order traversal
        if not tree:
            return;
        
        find_largest_helper(tree.right)

        if len(largest_elements) < k:
            largest_elements.append(tree.data)
        else:
            return;

        find_largest_helper(tree.left)

        return;
    
    largest_elements: List[int] = []
    find_largest_helper(tree)
    return largest_elements;


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
