# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, preorder, l, r):
        if l>r: return None
        v = preorder[self.idx]
        self.idx+=1
        m = self.dic[v]
        root = TreeNode(v)
        root.left = self.build(preorder, l, m-1)
        root.right = self.build(preorder, m+1,r)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.dic = {}
        self.idx = 0
        for i,n in enumerate(inorder):
            self.dic[n] = i
        root=self.build(preorder, 0, len(preorder)-1)
        return root