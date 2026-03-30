class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        i = 0
        head = self.head
        while head and i < index:
            i += 1
            head = head.next
        
        if head:
            return head.value
        return -1


    def insertHead(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.tail = node
        node.next = self.head
        self.head = node


    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
            elif self.head == self.tail:
                self.head = None
                self.tail = None
                return True
            else:
                self.head = self.head.next
                return True
        i = 0
        head = self.head
        prev = None
        while head and i < index:
            i += 1
            prev = head
            head = head.next
        
        if head:
            if head == self.tail:
                self.tail = prev
            prev.next = head.next
            del head
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        res = []
        head = self.head

        while head:
            res.append(head.value)
            head = head.next

        return res