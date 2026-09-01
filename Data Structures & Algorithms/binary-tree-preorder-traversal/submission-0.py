# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, ls):
        if root is None: return None
        ls.append(root.val)
        self.preorder(root.left, ls)
        self.preorder(root.right, ls)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.preorder(root, ls)
        return ls