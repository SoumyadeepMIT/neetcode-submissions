# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, root, mtl):
        if not root: return 0
        c = 0
        if root.val>=mtl: c = 1
        mtlc = max(mtl, root.val)
        return c + self.count(root.left, mtlc) + self.count(root.right, mtlc)

    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, -101) 