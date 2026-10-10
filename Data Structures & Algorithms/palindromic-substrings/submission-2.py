class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = 0
        for i in range(n):
            res+=1
            dp[i][i] = True
            if i<n-1:
                if s[i] == s[i+1]:
                    res+=1
                    dp[i][i+1] = True
        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res+=1
        return res