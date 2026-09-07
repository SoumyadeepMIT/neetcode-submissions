"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self, node):
        if node in self.dic.keys():
            return self.dic[node]
        nod = Node(node.val)
        self.dic[node] = nod
        for nei in node.neighbors:
            nei_nod = self.clone(nei)
            nod.neighbors.append(nei_nod)
        return nod

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        self.dic = {}
        nod = self.clone(node)
        return nod