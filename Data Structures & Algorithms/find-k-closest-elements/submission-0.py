class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while l<r:
            mid = l+(r-l)//2
            if arr[mid]<x:
                l = mid+1
            else:
                r = mid
        l, r = r-1,r
        while r-l-1<k:
            if l<0: r+=1
            elif r>=len(arr): l-=1
            elif abs(arr[r] - x)>=abs(arr[l]-x):
                l-=1
            else:
                r+=1
        return arr[l+1:r]