# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calc(self, root):
        if not root: return 0
        lv = max(self.calc(root.left), 0)
        rv = max(self.calc(root.right), 0)
        self.res = max(self.res, root.val + lv+rv)
        return root.val + max(lv,rv)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.calc(root)
        return int(self.res)