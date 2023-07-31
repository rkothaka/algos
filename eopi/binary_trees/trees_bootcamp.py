from binary_trees.binary_tree_node import BinaryTreeNode
from collections import deque


def tree_traversal(root: BinaryTreeNode):
    preorder = deque()
    inorder = deque()
    postorder = deque()
    if root:
        preorder.append(root.data)
        tree_traversal(root.left)
        inorder.append(root.data)
        tree_traversal(root.right)
        postorder.append(root.data)

