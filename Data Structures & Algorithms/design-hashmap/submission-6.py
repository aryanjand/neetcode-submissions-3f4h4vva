class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.map = [ListNode(None, None) for _ in range(9973)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            # Case 1: Key Already in the map
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        # Case 2: Key not in the map
        if not cur.next:
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[key % len(self.map)]
        while cur.next:
            # Case 1: Key is in the map
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        # Case 2: Key is not in the map
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            # Case 1: Key Already in the map
            if cur.next.key == key:
                cur.next = cur.next.next if cur.next else None
                return
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
