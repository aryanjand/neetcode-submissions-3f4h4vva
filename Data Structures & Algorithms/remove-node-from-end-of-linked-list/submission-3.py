# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse 1
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Delete node
        reversed_head = prev
        prev, curr = None, reversed_head
        index = 1
        while index < n:
            index += 1
            prev = curr
            curr = curr.next
        if not prev:
            reversed_head = reversed_head.next
        else:
            prev.next = curr.next

        # reverse 2
        prev, curr = None, reversed_head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
