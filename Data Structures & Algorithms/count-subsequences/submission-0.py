class Solution:
    def count(self, s, t, n, m, i, j):
        if j==m: return 1
        if i >=n: return 0
        if self.dp[i][j]!=-1: return self.dp[i][j]
        if s[i] == t[j]:
            self.dp[i][j] = self.count(s, t, n, m, i+1, j) + self.count(s, t, n, m, i+1, j+1)
        else:
            self.dp[i][j] = self.count(s,t,n,m,i+1,j)
        return self.dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        self.dp = [[-1]*m for _ in range(n)]
        return self.count(s, t, n, m, 0, 0)