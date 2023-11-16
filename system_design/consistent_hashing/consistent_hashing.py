import hashlib


class ConsistentHashing:
    def __init__(self, nodes=None, replica_count=3):
        self.nodes = nodes or []
        self.replica_count = replica_count
        self.hash_ring = {}
        self.sorted_keys = []

        self._initialize_hash_ring()

    def _initialize_hash_ring(self):
        for node in self.nodes:
            for i in range(self.replica_count):
                virtual_node = f"{node}_replica_{i}"
                hash_value = self._hash(virtual_node)
                self.hash_ring[hash_value] = node
                self.sorted_keys.append(hash_value)

        self.sorted_keys.sort()

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def get_node(self, key):
        if not self.nodes:
            return None

        hash_value = self._hash(key)
        for ring_key in self.sorted_keys:
            if hash_value <= ring_key:
                return self.hash_ring[ring_key]

        return self.hash_ring[self.sorted_keys[0]]

    def add_node(self, node):
        for i in range(self.replica_count):
            virtual_node = f"{node}_replica_{i}"
            hash_value = self._hash(virtual_node)
            self.hash_ring[hash_value] = node
            self.sorted_keys.append(hash_value)

        self.sorted_keys.sort()
        self.nodes.append(node)

    def remove_node(self, node):
        for i in range(self.replica_count):
            virtual_node = f"{node}_replica_{i}"
            hash_value = self._hash(virtual_node)
            if hash_value in self.hash_ring:
                del self.hash_ring[hash_value]
                self.sorted_keys.remove(hash_value)

        self.nodes.remove(node)
