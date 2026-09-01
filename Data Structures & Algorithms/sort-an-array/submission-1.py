class Solution:
    def merge(self, nums, l, m, r):
        left = nums[l:m+1]
        right = nums[m+1:r+1]
        k = l
        i = 0
        j = 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
        
    def mergesort(self, nums, l, r):
        if l>=r: return
        m = (l+r)//2
        self.mergesort(nums, l,m)
        self.mergesort(nums, m+1,r)
        self.merge(nums, l, m, r)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergesort(nums, 0, n-1)
        return nums