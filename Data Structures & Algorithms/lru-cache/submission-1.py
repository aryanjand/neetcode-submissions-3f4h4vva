from typing import Optional

class ListNode:
    def __init__(self, key: int, value: int, nxt: Optional['ListNode'] = None, prev: Optional['ListNode'] = None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.left = ListNode(0, 0) # LRU
        self.right = ListNode(0, 0) # MRU
        self.left.nxt, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru_node = self.left.nxt
            self._remove(lru_node)
            self.cache.pop(lru_node.key)
        
        node = ListNode(key, value)
        self._insert(node)
        self.cache[key] = node
    

    def _insert(self, node: ListNode) -> None:
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def _remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev