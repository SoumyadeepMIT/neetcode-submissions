class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2: return False
        tot //= 2
        dp = [False] * (tot + 1)
        dp[0] = True
        for num in nums:
            for j in range(tot, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        return dp[tot]