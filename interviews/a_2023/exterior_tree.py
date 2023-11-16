class TreeNode:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


def left_to_right_exterior_list(tree: TreeNode):
    if not tree:
        raise ValueError("Tree is empty/None")

    outer = [-1]
    result = [tree.data]

    def traversal(node: TreeNode, height: int):
        if not node.children:
            return

        height += 1
        children = node.children
        if len(outer) == height:
            outer.append([children[0], children[-1]])
        else:
            outer[height][1] = children[-1]

        for child in children:
            traversal(child, height)

        height -= 1

    traversal(tree, 0)
    for nodes in outer[1:]:
        result.insert(0, nodes[0].data)
        result.append(nodes[1].data)

    return result


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

    result = left_to_right_exterior_list(root)
    print(result)  # ['J', 'E', 'B', 'A', 'D', 'I', 'K']
