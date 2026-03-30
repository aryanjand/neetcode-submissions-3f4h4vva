# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        i = 0
        while i < n:
            i += 1
            right = right.next
        
        prev = None
        while right:
            prev = left
            left = left.next
            right = right.next
        if not prev:
            head = head.next
        else:
            prev.next = left.next
            del left

        return head