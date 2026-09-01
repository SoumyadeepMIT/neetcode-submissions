class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mtl = prices[n-1]
        res = 0
        for i in range(n-2,-1,-1):
            res = max(res, mtl - prices[i])
            mtl = max(mtl, prices[i])
        return res