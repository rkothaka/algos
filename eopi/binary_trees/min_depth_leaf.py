class TreeNode:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


def min_depth_leaf(root: TreeNode) -> int:
    if not root:
        raise ValueError('Invalid input: Empty Tree')

    def min_depth_helper(node: TreeNode, height: int):
        if not node.children:
            return height

        return min([min_depth_helper(child, height + 1) for child in node.children])

    return min_depth_helper(root, 0)


if __name__ == "__main__":
    root = TreeNode('A')
    root.children = [TreeNode('B'), TreeNode('C'), TreeNode('D')]
    root.children[0].children = [TreeNode('E'), TreeNode('F')]
    root.children[2].children = [TreeNode('G'), TreeNode('H'), TreeNode('I')]
    root.children[2].children[0].children = [TreeNode('J')]
    root.children[2].children[2].children = [TreeNode('K')]
    #       A
    #    /  |  \
    #   B   C   D
    #  / \     / | \
    # E   F   G  H  I
    #          |     \
    #          J      K

    result = min_depth_leaf(root)
    print(result)  # 1
