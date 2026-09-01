# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        qu = collections.deque()
        qu.append(root)
        res = []
        while qu:
            l = len(qu)
            lv = []
            for _ in range(l):
                nod = qu.popleft()
                lv.append(nod.val)
                if nod.left:
                    qu.append(nod.left)
                if nod.right:
                    qu.append(nod.right)
            res.append(lv[-1])
        return res 