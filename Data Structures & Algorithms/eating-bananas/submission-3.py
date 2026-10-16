class Solution:
    def count(self, piles, rate, h):
        hours = 0
        for p in piles:
            hours += (p + rate - 1) // rate   # ceil(p / rate)
            if hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            m = l+((r-l)//2)
            if self.count(piles, m, h):
                r = m
            else:
                l=m+1
        return l

