# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        cur = head

        for _ in range(left - 1):
            first = cur
            cur = cur.next

        prev = None
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        first.next.next = cur
        first.next = prev

        return dummy.next