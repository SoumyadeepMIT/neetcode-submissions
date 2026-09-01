class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x//2 + 1
        while l<r:
            mid = l+(r-l)//2
            if mid * mid < x:
                l = mid+1
            else:
                r = mid
        if r*r == x: return r
        return r-1