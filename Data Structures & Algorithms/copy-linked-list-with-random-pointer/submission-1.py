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
        dummy = Node(0)
        nod = dummy
        cur = head
        dic = {}
        while cur:
            nod.next = Node(cur.val)
            nod = nod.next
            dic[cur] = nod
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                nod=dic[cur]
                nod.random = dic[cur.random]
            cur = cur.next
        return dummy.next
