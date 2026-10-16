class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = max(heights)
        n = len(heights)
        for i in range(n):
            ind = i
            while len(st)>0 and st[-1][0]>=heights[i]:
                ind = st[-1][1]
                res = max(res, st[-1][0]*(i-st[-1][1]))
                st.pop()
            res = max(res, heights[i] * (i-ind+1))
            st.append((heights[i], ind))
        while len(st)>0:
            res = max(res, st[-1][0] * (n - st[-1][1]))
            st.pop()
        return res