# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        i = 1
        dic = {}
        while cur:
            dic[i] = cur
            cur = cur.next
            i+=1
        while left<right:
            curl = dic[left]
            curr = dic[right]
            t = curl.val
            curl.val = curr.val
            curr.val = t
            left+=1
            right-=1
        return head