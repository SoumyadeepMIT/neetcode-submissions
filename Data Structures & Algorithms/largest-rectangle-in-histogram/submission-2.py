class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1]>h:
                ind, hei = st.pop()
                res = max(res, hei*(i - ind))
                start = ind
            st.append((start, h))
        
        for i,h in st:
            res = max(res, h*(len(heights) - i))
        return res