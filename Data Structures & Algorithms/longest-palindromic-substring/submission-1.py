class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        resLen = 1
        resIdx = 0
        for i in range(n):
            if i<n-1:
                if s[i] == s[i+1]: 
                    dp[i][i+1] = True
                    resLen = 2
                    resIdx = i
            dp[i][i] = True
        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if resLen<l:
                        resLen = l
                        resIdx = i
        return s[resIdx: resIdx + resLen]