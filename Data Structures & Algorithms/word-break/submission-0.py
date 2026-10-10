class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        wd = set(wordDict)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i:j+1] in wd and dp[j+1]:
                    dp[i] = True
        return dp[0]