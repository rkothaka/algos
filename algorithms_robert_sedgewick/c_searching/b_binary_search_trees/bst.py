from collections import deque


class BST:
    class Node:
        def __init__(self, key, val, left=None, right=None, n=1):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.n = n

    def __init__(self):
        self.root = None

    def __bool__(self):
        return self.root

    def empty(self):
        return not self

    def __len__(self):
        if self.root:
            return self.root.n
        else:
            return 0

    def size(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return node.n

    def get(self, key, x=None):
        if x is None:
            x = self.root

        if x is None:
            return None

        cmp = key - x.key
        if cmp < 0:
            return self.get(key, x.left)
        elif cmp > 0:
            return self.get(key, x.right)
        else:
            return x.value

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return BST.Node(key, val)

        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        x.n = self.size(x.left) + self.size(x.right) + 1
        return x

    def min(self):
        if self.empty():
            raise KeyError("BST is empty, no minimum element")
        return self._min(self.root)

    def _min(self, x):
        if x.left:
            return self._min(x.left)
        return x

    def max(self):
        if self.empty():
            raise KeyError("BST is empty, no maximum element")
        return self._max(self.root)

    def _max(self, x):
        if x.right:
            return self._max(x.right)
        return x

    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None:
            raise KeyError("No such element exception")
        return x.key

    def _floor(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        elif key < node.key:
            return self._floor(node.left, key)
        else:
            f = self._floor(node.right, key)
            if f:
                return f
            else:
                return node

    def select(self, k):
        if k < 0 or k >= self.size():
            raise ValueError("K is out of bounds")
        node = self._select(self.root, k)
        return node.key

    def _select(self, node, k):
        if node is None:
            return None
        t = self.size(node.left)
        if k < t:
            return self._select(node.left, k)
        elif k > t:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self.size(node.left) + self._rank(node.right, key)
        else:
            return self.size(node.left)

    def delete_min(self):
        if self.empty():
            raise KeyError("BST is empty, no minimum element to delete.")
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.n = self.size(node.left) + self.size(node.right) + 1
        return node

    def delete(self, key):
        if self.empty():
            raise KeyError("BST is empty, no element to delete.")
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            self._delete(node.left, key)
        elif key > node.key:
            self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            temp_node = node
            node = self._min(temp_node.right)
            node.right = self._delete_min(temp_node.right)
            node.left = temp_node.left

        node.n = self.size(node.left) + self.size(node.right) + 1
        return node

    def range_iter(self):
        return self._range_iter(self.min(), self.max())

    def _range_iter(self, lo, hi):
        queue = deque()

        def _range_iter_helper(node):
            if node is None:
                return
            if lo < node.key:
                _range_iter_helper(node.left)
            if lo <= node.key <= hi:
                queue.append(node.key)
            if hi > node.key:
                _range_iter_helper(node.right)

        _range_iter_helper(self.root)
        return queue
