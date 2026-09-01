# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p, q):
        if p and q:
            if p.val != q.val: return False
            return (self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right))
        elif not p and not q: return True
        else: return False  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.isSameTree(root, subRoot) | self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)