import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_possible_fbt(n: int) -> List[Optional[TreeNode]]:
    if n <= 0:
        return None

    result_set = []
    root, n = TreeNode(), n-1
    result_set.append(root)

    def clone_tree(root: TreeNode):
        if not root:
            return None

        cloned_tree_root = TreeNode(root.val)
        cloned_tree_root.left = clone_tree(root.left)
        cloned_tree_root.right = clone_tree(root.right)
        return cloned_tree_root

    def generate_fbt():
        temp_result_set = []
        for element in result_set:
            traversal(element, element, temp_result_set)
        print(temp_result_set)
        return temp_result_set

    def traversal(root, node, temp_result_set):
        if node.left is None and node.right is None:
            node.left, node.right = TreeNode(), TreeNode()
            temp_result_set.append(clone_tree(root))
            node.left, node.right = None, None
            return
        else:
            traversal(root, node.right, temp_result_set)
            traversal(root, node.left, temp_result_set)

    while n:
        result_set = generate_fbt()
        n -= 2

    return result_set


if __name__ == "__main__":
    print(all_possible_fbt(7))

