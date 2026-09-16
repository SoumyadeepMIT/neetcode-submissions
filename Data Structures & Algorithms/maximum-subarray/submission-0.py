class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        s = 0
        for n in nums:
            s = max(n, s+n)
            res = max(res, s)
        return res