from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    if not tree:
        return result

    current_depth_nodes = [tree]
    while current_depth_nodes:
        result.append([n.data for n in current_depth_nodes])
        current_depth_nodes = [child for parent in current_depth_nodes for child in (parent.left, parent.right) if child]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
