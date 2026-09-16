class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxp = nums[0]
        i = 1
        while i<n:
            if i>maxp: return False
            maxp = max(i+nums[i], maxp)
            i+=1
        return maxp>=(n-1)