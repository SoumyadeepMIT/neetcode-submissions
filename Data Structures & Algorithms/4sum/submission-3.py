class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]: continue
                l, r = j+1, n-1
                while l<r:
                    sumv = nums[i] + nums[j] + nums[l] + nums[r]
                    if sumv<target:
                        l+=1
                    elif sumv>target:
                        r-=1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]: l+=1
        return res