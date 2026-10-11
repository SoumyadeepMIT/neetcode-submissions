class Solution:
    def check(self, s1, s2, s3, n, m, l, i, j, k):
        if k==l: return (i==n and j==m)
        if (i, j) in self.dp: return self.dp[(i, j)]
        self.dp[(i, j)] = False
        if i<n and s1[i] == s3[k]:
            self.dp[(i,j)] = self.dp[(i,j)] or self.check(s1, s2, s3, n, m, l, i+1, j, k+1)
        if j<m and not self.dp[(i,j)] and s2[j] == s3[k]:
            self.dp[(i,j)] = self.dp[(i,j)] or self.check(s1, s2, s3, n, m, l, i, j+1, k+1)
        return self.dp[(i,j)]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if (n+m) != l: return False
        self.dp = {}
        return self.check(s1, s2, s3, n, m, l, 0, 0, 0)