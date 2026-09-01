class Solution:
    def merge(self,arr: List[int], l:int, m:int, r:int):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        k = l
        i = 0
        j = 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            k+=1
            i+=1
        while j<len(right):
            arr[k] = right[j]
            k+=1
            j+=1
    
    def mergesort(self,arr:List[int], l:int, r:int):
        if l>=r: return
        m = (l+r)//2
        self.mergesort(arr, l,m)
        self.mergesort(arr, m+1, r)
        self.merge(arr, l,m,r)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergesort(nums, 0, n-1)
        return nums
        