from typing import Optional
from eopi.bst.bst import TreeNode


def search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val == val:
        return root
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)


