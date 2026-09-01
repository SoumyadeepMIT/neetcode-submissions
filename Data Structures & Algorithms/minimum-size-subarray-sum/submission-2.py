class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        sumv = 0
        res = n+1
        while r<n:
            sumv += nums[r]
            while l<=r and sumv>=target:
                res = min(res, r-l+1)
                sumv -= nums[l]
                l+=1
            r+=1
        if res == n+1: return 0
        return res