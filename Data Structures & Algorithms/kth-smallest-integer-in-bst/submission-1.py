class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = -1
        self.kth(root)
        return self.res

    def kth(self, root):
        if not root:
            return
        self.kth(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.kth(root.right)