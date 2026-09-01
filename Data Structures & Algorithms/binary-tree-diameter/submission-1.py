# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root) ->int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        dia = self.maxDepth(root.left) + self.maxDepth(root.right)
        return max(dia, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))