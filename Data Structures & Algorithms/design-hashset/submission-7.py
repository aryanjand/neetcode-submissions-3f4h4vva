class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(None) for _ in range(10**4)]

    def add(self, key: int) -> None:
        node = self.set[key % len(self.set)]
        while node or node.nxt:
            if node.val == key:
                return None
            if not node.nxt:
                break
            node = node.nxt
        node.nxt = ListNode(key)

    def remove(self, key: int) -> None:
        node = self.set[key % len(self.set)]
        while node.nxt and node.nxt.val != key:
            node = node.nxt
        node.nxt = node.nxt.nxt if node.nxt else None

    def contains(self, key: int) -> bool:
        node = self.set[key % len(self.set)]
        while node:
            if node.val == key:
                return True
            node = node.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)