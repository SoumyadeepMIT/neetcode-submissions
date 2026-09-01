class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        ml = 0
        for n in nums:
            if n-1 in dic: continue
            l = 0
            temp = n
            while temp in dic:
                l+=1
                temp += 1
            ml = max(ml, l)
        return ml

