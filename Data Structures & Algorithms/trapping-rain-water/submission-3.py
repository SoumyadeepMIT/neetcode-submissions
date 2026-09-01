class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]
        res = 0
        while l<r:
            if lm<rm:
                l+=1
                lm = max(lm, height[l])
                res+= (lm - height[l])
            else:
                r-=1
                rm = max(rm, height[r])
                res+= (rm - height[r])
        return res