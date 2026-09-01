class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]<=nums[r]:
                r = mid
            else:
                l = mid+1
        piv = l
        l,r = 0,len(nums)-1
        if target>=nums[piv] and target<=nums[r]:
            l = piv
        else:
            r = piv-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif target<nums[mid]:
                r=mid-1
            else:
                l = mid+1
        return -1