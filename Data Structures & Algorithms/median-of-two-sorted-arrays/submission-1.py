class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        l,r = 0, len(nums1)
        total = len(nums1) + len(nums2)
        half = total // 2
        while l<=r:
            i = l+(r-l)//2
            j = half - i
            aleft = float('-inf') if i==0 else nums1[i-1]
            aright = float('inf') if i==len(nums1) else nums1[i]
            bleft = float('-inf') if j==0 else nums2[j-1]
            bright = float('inf') if j==len(nums2) else nums2[j]
            if aleft<= bright and bleft<=aright:
                if total%2==0:
                    return (max(aleft, bleft) + min(aright, bright))/2
                else:
                    return min(aright, bright)
            elif aleft>bright:
                r=i-1
            else:
                l = i+1
        return -1