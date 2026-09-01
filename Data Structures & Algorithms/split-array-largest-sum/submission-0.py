class Solution:
    def check(self, nums, s):
        c = 1
        cur = 0
        for n in nums:
            if cur + n>s:
                cur = 0
                c+=1
            cur+=n
        return c

    def splitArray(self, nums: List[int], k: int) -> int:
        l= max(nums)
        r = sum(nums)
        res = r
        while l<=r:
            m = l+(r-l)//2
            if self.check(nums,m)<=k:
                res = m
                r = m-1
            else:
                l = m+1
        return res
