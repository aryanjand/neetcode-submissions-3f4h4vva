"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr = head

        while curr:
            newNode = Node(curr.val)
            nodeMap[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = nodeMap[curr]
            copyNode.next = nodeMap[curr.next] if curr.next else None
            copyNode.random = nodeMap[curr.random] if curr.random else None
            curr = curr.next
        
        return nodeMap[head] if head else None