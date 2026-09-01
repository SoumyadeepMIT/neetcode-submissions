class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lpref = [1] * (n+2)
        rpref = [1] * (n+2)
        for i in range(1, n+1):
            lpref[i] = lpref[i-1] * nums[i-1]
        for i in range(n, 0, -1):
            rpref[i] = rpref[i+1] * nums[i-1]
        res = []
        for i in range(1,n+1):
            res.append(lpref[i-1] * rpref[i+1])
        return res