class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        res = 0
        sumset = {0:1}
        for num in nums:
            pref+=num
            if (pref - k) in sumset: 
                res+=sumset[(pref-k)]
            sumset[pref] = 1 + sumset.get(pref, 0)
        return res
