class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Hashmap
        self.map = {}
        # Linked List
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._insert(node)
            node.value = value
            return None
        
        node = ListNode(key, value)
        self._insert(node)
        self.map[key] = node

        capacity = len(self.map)
        if capacity > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]


    def _remove(self, node: Optional[ListNode]) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node: Optional[ListNode]) -> None:
        prev, next = self.tail.prev, self.tail
        node.prev, node.next = prev, next
        prev.next = next.prev = node
        