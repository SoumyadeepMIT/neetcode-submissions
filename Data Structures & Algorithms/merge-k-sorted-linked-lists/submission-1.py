# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <=list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        while list1:
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next
        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n==0:
            return None
        while n>1:
            for i in range(n//2):
                lists[i] = self.mergeTwoLists(lists[i], lists[n-i-1])
            n = (n+1)//2
        return lists[0]
        