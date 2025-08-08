import collections
import functools
from turtle import right
from typing import Optional
from xxlimited import Null

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    Status = collections.namedtuple('Status', ('number_of_target_nodes', 'lca'))
    
    def find_lca(tree, node0, node1):
        if tree is None:
            return Status(0, None)

        left_status = find_lca(tree.left, node0, node1)
        if left_status.number_of_target_nodes == 2:
            return left_status
        
        right_status = find_lca(tree.right, node0, node1)
        if right_status.number_of_target_nodes == 2:
            return right_status
        
        number_of_nodes = left_status.number_of_target_nodes + right_status.number_of_target_nodes + (node0, node1).count(tree)
        return Status(number_of_nodes, tree if number_of_nodes == 2 else None)
    return find_lca(tree, node0, node1).lca


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
