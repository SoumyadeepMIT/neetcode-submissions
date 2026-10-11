class Solution:
    def mp(self, prices, n, i, sell):
        if i >= n: return 0
        if self.dp[i][sell]!=-1: return self.dp[i][sell]
        if sell==0:
            self.dp[i][sell] =  max(-prices[i] + self.mp(prices, n, i+1, 1), self.mp(prices, n, i+1, 0))
        else:
            self.dp[i][sell] =  max(prices[i] + self.mp(prices, n, i+2, 0), self.mp(prices, n, i+1, 1))
        return self.dp[i][sell]
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        self.dp = [[-1]*2 for _ in range(n)]
        return self.mp(prices, n, 0, 0)