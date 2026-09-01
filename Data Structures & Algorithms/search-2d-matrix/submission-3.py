class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bot = row - 1
        while top<=bot:
            mid = top + (bot-top)//2
            if matrix[mid][0] == target or matrix[mid][col-1] == target:
                return True
            elif target>matrix[mid][col-1]:
                top = mid+1
            elif target<matrix[mid][0]:
                bot = mid-1
            else:break
        if top>bot: return False
        l = 0
        r = col-1
        row = (top+bot)//2
        while l<=r:
            mid = l + (r-l)//2
            if target == matrix[row][mid]: return True
            elif target <matrix[row][mid]: r = mid-1
            else: l = mid+1
        return False