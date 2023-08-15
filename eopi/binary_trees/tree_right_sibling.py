from eopi.binary_trees.binary_tree_node import TreeNode


def construct_right_sibling(tree: TreeNode) -> None:
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            start_node.left.next = start_node.right
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left
