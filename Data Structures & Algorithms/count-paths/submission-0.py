class Solution:
    def up(self, m, n):
        if m==0 and n==0:
            return 1
        if m<0 or n<0: return 0
        if self.dp[m][n] != -1 : return self.dp[m][n]
        self.dp[m][n] = self.up(m-1, n) + self.up(m, n-1)
        return self.dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[-1]*n for _ in range(m)]
        return self.up(m-1, n-1)
        