class Solution:
    def count(self, nums, target, n, i, cur):
        if i>=n:
            if cur==target: return 1
            else: return 0
        if cur in self.dp[i]: return self.dp[i][cur]
        self.dp[i][cur] =  self.count(nums, target, n, i+1, cur+nums[i]) + self.count(nums, target, n, i+1, cur-nums[i])
        return self.dp[i][cur]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.dp = [{} for _ in range(n)]
        return self.count(nums, target, n,  0, 0)