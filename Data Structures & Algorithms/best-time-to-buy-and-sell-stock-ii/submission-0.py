class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+1)]
        def rec(i, buy):
            if i == n: return 0
            if dp[i][buy] != -1: return dp[i][buy]
            res = rec(i+1, buy)
            if buy:
                res = max(res, -prices[i] + rec(i+1, False))
            else:
                res = max(res, prices[i] + rec(i+1, True))
            dp[i][buy] = res
            return res
        return rec(0, True)