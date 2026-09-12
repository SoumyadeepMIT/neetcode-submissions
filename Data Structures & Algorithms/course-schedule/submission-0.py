class Solution:
    def dfs(self, n):
        if self.vis[n] == 1: return True
        if self.vis[n] == 2: return False
        self.vis[n] = 1
        for nei in self.adj[n]:
            if self.dfs(nei): return True
        self.vis[n] = 2
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            self.adj[pre[1]].append(pre[0])
        self.vis = [0] * numCourses
        for i in range(numCourses):
            if self.vis[i] == 0:
                if self.dfs(i): return False
        return True