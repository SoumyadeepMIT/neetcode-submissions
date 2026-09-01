# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, ls):
        if root is None: return None
        self.inorder(root.left, ls)
        ls.append(root.val)
        self.inorder(root.right, ls)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.inorder(root, ls)
        return ls