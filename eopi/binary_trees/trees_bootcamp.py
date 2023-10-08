from binary_tree_node import TreeNode
from collections import deque


def tree_traversal(root: TreeNode):
    preorder = deque()
    inorder = deque()
    postorder = deque()
    if root:
        preorder.append(root.data)
        tree_traversal(root.left)
        inorder.append(root.data)
        tree_traversal(root.right)
        postorder.append(root.data)

