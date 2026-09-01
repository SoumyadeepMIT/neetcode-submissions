class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        curr = nums[0]
        n = len(nums)
        i = 1
        while i<n:
            j = i
            while j<n and nums[j] == curr: j+=1
            if j==n:break
            curr = nums[j]
            i = j+1
            nums[ind] = curr
            ind+=1
        return ind