class Solution:
    def isValid(self, i, j, n, m):
        if i<0 or j<0 or i>=n or j>=m:
            return False
        if self.vis[i][j]: return False
        return True
    def dfs(self, i, j, n, m, ls):
        if self.vis[i][j]:
            return None
        self.vis[i][j] = True
        ls.append((i, j))
        if self.isValid(i+1, j, n, m) and self.heights[i+1][j]>=self.heights[i][j]:
            self.dfs(i+1, j, n, m, ls)
        if self.isValid(i-1, j, n, m) and self.heights[i-1][j]>=self.heights[i][j]:
            self.dfs(i-1, j, n, m, ls)
        if self.isValid(i, j+1, n, m) and self.heights[i][j+1]>=self.heights[i][j]:
            self.dfs(i, j+1, n, m, ls)
        if self.isValid(i, j-1, n, m) and self.heights[i][j-1]>=self.heights[i][j]:
            self.dfs(i, j-1, n, m, ls)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        n = len(heights)
        m = len(heights[0])
        self.vis = [[False]*m for _ in range(n)]
        pac = []
        atl = []
        for i in range(m):
            if not self.vis[0][i]:
                self.dfs(0, i, n, m, pac)
        for i in range(n):
            if not self.vis[i][0]:
                self.dfs(i, 0, n, m, pac)
        self.vis = [[False]*m for _ in range(n)]
        for i in range(m):
            if not self.vis[n-1][i]:
                self.dfs(n-1, i, n, m, atl)
        for i in range(n):
            if not self.vis[i][m-1]:
                self.dfs(i, m-1, n, m, atl)
        pac_set = set(pac)
        res = []
        for n in atl:
            if n in pac_set:
                res.append([n[0], n[1]])
        return res
