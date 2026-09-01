class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.pref = [[0 for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1,r+1):
            sumv = 0
            for j in range(1, c+1):
                sumv+=matrix[i-1][j-1]
                self.pref[i][j] = sumv + self.pref[i-1][j] 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pref[row2+1][col2+1] - self.pref[row1][col2+1] - self.pref[row2+1][col1] + self.pref[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)