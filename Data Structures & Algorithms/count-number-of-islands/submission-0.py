from collections import deque
class Solution:
    def isVal(self, i, j, m, n):
        if i<0 or j<0 or i>=m or j>=n:
            return False
        return True
    def bfs(self, grid, vis, i, j):
        qu = deque()
        qu.append((i, j))
        m = len(grid)
        n = len(grid[0])
        while len(qu) != 0:
            x, y = qu.popleft()
            if self.isVal(x+1, y, m, n) and not vis[x+1][y] and grid[x+1][y] == "1":
                qu.append((x+1, y))
                vis[x+1][y] = True
            if self.isVal(x-1, y, m, n) and not vis[x-1][y] and grid[x-1][y] == "1":
                qu.append((x-1, y))
                vis[x-1][y] = True
            if self.isVal(x, y+1, m, n) and not vis[x][y+1] and grid[x][y+1] == "1":
                qu.append((x, y+1))
                vis[x][y+1] = True
            if self.isVal(x, y-1, m, n) and not vis[x][y-1] and grid[x][y-1] == "1":
                qu.append((x, y-1))
                vis[x][y-1] = True
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (not vis[i][j]):
                    self.bfs(grid, vis, i, j)
                    res+=1
        return res