class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        curp = 0
        maxp = 0
        jumps = 0
        for i in range(n):
            maxp = max(maxp, i+nums[i])
            if maxp>=(n-1):
                return jumps + 1
            if i == curp:
                if i == maxp: return -1
                curp = maxp
                jumps+=1
        return jumps