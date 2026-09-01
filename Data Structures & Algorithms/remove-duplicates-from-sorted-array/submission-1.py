class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = nums[0]
        ind = 1
        i = 1
        while i<len(nums):
            while i<len(nums) and nums[i]==n:
                i+=1
            if i==len(nums): break
            nums[ind] = nums[i]
            ind+=1
            n = nums[i]
            i+=1
        return ind