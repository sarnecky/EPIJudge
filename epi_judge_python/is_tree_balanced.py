from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def check_balance(node) -> tuple[bool, int]:
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1

        return balanced, height

    return check_balance(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
