class Solution:
    def lcs(self, text1, text2, n, m, i, j):
        if i>=n or j>=m: return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        res = 0
        if text1[i] == text2[j]:
            res = 1+self.lcs(text1, text2, n, m , i+1, j+1)
        res = max([res, self.lcs(text1, text2, n, m, i, j+1), self.lcs(text1, text2, n, m, i+1, j)])
        self.dp[i][j] = res
        return res
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        self.dp = [[-1]*m for _ in range(n)]
        return self.lcs(text1, text2, n, m, 0, 0)