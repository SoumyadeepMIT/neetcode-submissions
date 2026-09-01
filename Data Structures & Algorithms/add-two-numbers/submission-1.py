# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            num = l1.val + l2.val + c
            c = num//10
            n = num%10
            cur.next = ListNode(n)
            cur, l1, l2 = cur.next, l1.next, l2.next

        while l1:
            num = l1.val + c
            c = num//10
            n = num%10
            cur.next = ListNode(n)
            cur, l1 = cur.next, l1.next
        
        while l2:
            num = l2.val + c
            c = num//10
            n = num%10
            cur.next = ListNode(n)
            cur, l2 = cur.next, l2.next
        if c!=0:
            cur.next = ListNode(c)
            cur = cur.next
        return dummy.next