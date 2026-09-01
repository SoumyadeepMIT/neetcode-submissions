# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root, ls):
        if not root: return None
        self.postorder(root.left, ls)
        self.postorder(root.right, ls)
        ls.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.postorder(root, ls)
        return ls