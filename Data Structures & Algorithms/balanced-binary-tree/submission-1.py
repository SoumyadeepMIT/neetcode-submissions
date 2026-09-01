# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root) -> int:
        if not root: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        lh = self.depth(root.left)
        rh = self.depth(root.right)
        if abs(lh-rh)>1:return False
        return self.isBalanced(root.left) & self.isBalanced(root.right)
        