class Solution:
    def check(self, weights, k, days):
        day, curr = 1, k
        for w in weights:
            if curr-w<0:
                day+=1
                if day>days:return False
                curr = k
            curr-=w
        return True
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            mid = l+(r-l)//2
            if self.check(weights, mid, days):
                res = mid
                r = mid-1
            else:
                l= mid+1
        return res