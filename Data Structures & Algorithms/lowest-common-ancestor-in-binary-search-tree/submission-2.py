# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        minv = min(p.val, q.val)
        maxv = max(p.val, q.val)
        if root.val>=minv and root.val<=maxv: return root
        if root.val<minv:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val>maxv:
            return self.lowestCommonAncestor(root.left, p, q)
        