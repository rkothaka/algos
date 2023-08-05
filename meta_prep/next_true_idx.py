class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def ceil_bst(self, key) -> int:
        node, equal_or_next_high = self.root, None
        while node:
            if node.key == key:
                return node.key
            if node.key > key:
                node, equal_or_next_high = node.left, node.key
            else:
                node = node.right

        return equal_or_next_high

    def __str__(self):
        return self._str_recursive(self.root)

    def _str_recursive(self, node):
        if node is None:
            return ''
        left_str = self._str_recursive(node.left)
        right_str = self._str_recursive(node.right)
        return f"{left_str} {node.key} {right_str}".strip()

    def __repr__(self):
        return f"BinarySearchTree({self.__str__()})"


class NextTrue:
    def __init__(self, N: int):
        self._N = N
        self.arr = [False] * (N + 1)
        self.bst = BinarySearchTree()

    @property
    def N(self):
        return self._N

    def set_true(self, idx: int) -> int:
        if not 1 <= idx <= self.N:
            raise ValueError(f'{idx} out of bounds. Acceptable range: [1, {self.N}]')

        if self.arr[idx]:  # Already marked as True
            return idx

        self.arr[idx] = True
        self.bst.insert(idx)
        return idx

    def next_true(self, idx: int) -> int:
        if not 1 <= idx <= self.N:
            raise ValueError(f'{idx} out of bounds. Acceptable range: [1, {self.N}]')

        result = self.bst.ceil_bst(idx)
        return result if result else -1

    def __str__(self):
        return f"NextTrue(N={self.N}, arr={self.arr}, bst={self.bst})"

    def __repr__(self):
        return f"NextTrue(arr={self.arr})"


if __name__ == '__main__':
    nt = NextTrue(10)
    print(nt)

    queries = [[1, 2], [2, 5], [2, 10], [1, 2], [2, 3], [1, 2], [1, 6], [1, 5]]
    # [-1, 5, 10, 5, 3, 3, 10, 5]
    # 1 - next_true
    # 2 - set_true

    result = []
    for query in queries:
        if query[0] == 1:
            result.append(nt.next_true(query[1]))
        else:
            result.append(nt.set_true(query[1]))

    print(nt)
    print(result)
