from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] = True
        res = 0
        for n in nums:
            if dic[n-1]: continue
            k = n
            l = 0
            while dic[k]:
                l+=1
                k+=1
            res = max(res, l)
        return res
