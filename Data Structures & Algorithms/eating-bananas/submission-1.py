class Solution:
    def check(self, piles, k):
        hrs = 0
        for p in piles:
            if p%k==0:
                hrs += (p//k)
            else:
                hrs += (p//k) + 1
        return hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1
        while l<=r:
            mid = l+(r-l)//2
            if self.check(piles, mid)<=h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res