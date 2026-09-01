# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serhelp(self, root):
        if not root:
            self.res.append("N")
            return
        self.res.append(str(root.val))
        self.serhelp(root.left)
        self.serhelp(root.right)

    def deserhelp(self, arr):
        if arr[self.idx] == "N":
            self.idx+=1
            return None
        nod = TreeNode(int(arr[self.idx]))
        self.idx+=1
        nod.left = self.deserhelp(arr)
        nod.right = self.deserhelp(arr)
        return nod
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.serhelp(root)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.idx = 0
        return self.deserhelp(arr)