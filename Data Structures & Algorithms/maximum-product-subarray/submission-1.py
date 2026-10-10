class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmin, cmax = 1, 1
        for num in nums:
            tmp = cmax * num
            cmax = max(cmax*num, num, cmin * num)
            cmin = min(tmp, num, cmin * num)
            res = max(res, cmax)
        return res