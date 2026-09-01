"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def check(self, grid, top, bottom, left, right):
        val = grid[top][left]
        for i in range(top, bottom):
            for j in range(left, right):
                if val != grid[i][j]:
                    nod = Node(val, 0, None, None, None, None)
                    return nod
        nod = Node(val, 1, None, None, None, None)
        return nod
    def cons(self, grid, top, bottom, left, right):
        nod = self.check(grid, top, bottom, left, right)
        if nod.isLeaf: return nod
        nod.topLeft = self.cons(grid, top, (top+bottom)//2, left, (left+right)//2)
        nod.topRight = self.cons(grid, top, (top+bottom)//2, (left+right)//2, right)
        nod.bottomLeft = self.cons(grid, (top+bottom)//2, bottom, left, (left+right)//2)
        nod.bottomRight = self.cons(grid, (top+bottom)//2, bottom, (left+right)//2, right)
        return nod
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        root = self.cons(grid, 0, n, 0, n)
        return root