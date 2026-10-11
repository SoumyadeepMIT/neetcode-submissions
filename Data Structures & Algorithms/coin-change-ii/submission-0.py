class Solution:
    def count(self, coins, n, i, amt):
        if amt == 0: return 1
        if amt<0: return 0
        if i>=n: return 0
        if self.dp[i][amt]!=-1: return self.dp[i][amt]
        self.dp[i][amt] = self.count(coins, n, i, amt - coins[i]) + self.count(coins, n, i+1, amt)
        return self.dp[i][amt]
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        self.dp = [[-1]*(amount+1) for _ in range(n)]
        return self.count(coins, n, 0, amount)