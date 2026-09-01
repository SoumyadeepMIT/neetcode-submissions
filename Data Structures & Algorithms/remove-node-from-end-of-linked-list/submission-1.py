# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nthfront = head
        dummy = ListNode(0, head)
        nth = dummy
        while n>0:
            nthfront = nthfront.next
            n-=1
        while nthfront:
            nth = nth.next
            nthfront = nthfront.next
        nth.next = nth.next.next
        return dummy.next