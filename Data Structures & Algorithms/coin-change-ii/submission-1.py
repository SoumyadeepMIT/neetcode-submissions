class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(n-1, -1, -1):
            for j in range(amount+1):
                if j-coins[i]>=0:
                    dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][amount]