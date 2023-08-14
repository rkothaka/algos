# Compute length of traversal between two nodes in a binary tree
# cannot use parent links
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal_length(root: TreeNode, node1: TreeNode, node2: TreeNode) -> int:
    def path(current_node, target_node, current_path):
        if current_node is None:
            return []

        current_path = current_path + [current_node.val]
        if current_node == target_node:
            return current_path

        left_path = path(current_node.left, target_node, current_path)
        if left_path:
            return left_path

        right_path = path(current_node.right, target_node, current_path)
        if right_path:
            return right_path

        return []

    node1_path = path(root, node1, [])
    node2_path = path(root, node2, [])
    print(node1_path)
    print(node2_path)

    if node1_path[0] != node2_path[0]:
        return -1

    common_depth = 0
    while node1_path[common_depth] == node2_path[common_depth]:
        common_depth += 1
        if common_depth == len(node1_path) or common_depth == len(node2_path):
            break

    return (len(node1_path) - common_depth) + (len(node2_path) - common_depth)


if __name__ == "__main__":
    A, B, D = TreeNode('A'), TreeNode('B'), TreeNode('D')
    E, F, G, I = TreeNode('E'), TreeNode('F'), TreeNode('G'), TreeNode('I')
    J, K = TreeNode('J'), TreeNode('K')
    root = A
    root.left, root.right = B, D
    root.left.left, root.left.right = E, F
    root.right.left, root.right.right = G, I
    root.right.left.left = J
    root.right.right.right = K
    #       A
    #    /    \
    #   B      D
    #  / \    /  \
    # E   F  G    I
    #        |     \
    #        J      K
    print(traversal_length(A, J, K))
