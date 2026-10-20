# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val: return root
        llca = self.lowestCommonAncestor(root.left, p, q)
        rlca = self.lowestCommonAncestor(root.right, p, q)
        if llca and rlca: return root
        return llca if llca else rlca