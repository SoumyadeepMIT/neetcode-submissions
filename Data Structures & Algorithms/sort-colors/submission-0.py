class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0
        for n in nums:
            if n==0: c0+=1
            elif n==1: c1+=1
            elif n==2: c2+=1
        k = 0
        s = 0
        while s<c0:
            nums[k] = 0
            k+=1
            s+=1
        s = 0
        while s<c1:
            nums[k] = 1
            k+=1
            s+=1
        s = 0
        while s<c2:
            nums[k] = 2
            k+=1
            s+=1
        