# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root):
        if root in self.dic: return self.dic[root]
        self.dic[root] = root.val
        if root.left:
            self.dic[root]+=(self.check(root.left.left) + self.check(root.left.right))
        if root.right:
            self.dic[root]+=(self.check(root.right.left) + self.check(root.right.right))
        self.dic[root] = max(self.dic[root], self.check(root.left) + self.check(root.right))
        return self.dic[root]
    def rob(self, root: Optional[TreeNode]) -> int:
        self.dic = {None: 0}
        return self.check(root)