# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, head):
        cur = head
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sec = self.rev(slow.next)
        slow.next = None
        cur1 = head
        cur2 = sec
        while cur1 and cur2:
            nx1, nx2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nx1
            cur1, cur2 = nx1, nx2
