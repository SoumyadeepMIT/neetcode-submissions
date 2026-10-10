class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
                res = max(res, lis[i])
        return res