# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, minv, maxv):
        if not root: return True
        if not (minv<root.val and root.val<maxv): return False
        return self.isValid(root.left, minv, root.val) and self.isValid(root.right, root.val, maxv)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -1001, 1001)
        