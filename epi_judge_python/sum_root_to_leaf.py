from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_root_to_leaf_healper(node, partial_path_sum):
        if not node:
            return 0
        
        partial_path_sum = partial_path_sum*2 + node.data
        if not node.left and not node.right:
            return partial_path_sum

        return sum_root_to_leaf_healper(node.left, partial_path_sum) + sum_root_to_leaf_healper(node.right, partial_path_sum)
    return sum_root_to_leaf_healper(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
