# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
   

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        

        left, right = head, prev
        while right:
            templ, tempr = left.next, right.next
            left.next = right
            right.next = templ
            left, right = templ, tempr
        