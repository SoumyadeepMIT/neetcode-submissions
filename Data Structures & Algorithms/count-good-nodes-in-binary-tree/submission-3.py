# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def cnodes(self, root, maxv):
        if not root: return
        if root.val>=maxv: self.count+=1
        maxv = max(root.val, maxv)
        self.cnodes(root.left, maxv)
        self.cnodes(root.right, maxv)
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.cnodes(root, -101)
        return self.count