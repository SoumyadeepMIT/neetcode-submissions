class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rows = [[False] * 10 for _ in range(10)]
        self.cols = [[False] * 10 for _ in range(10)]
        self.sq = [[False] * 10 for _ in range(10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if self.rows[i][int(board[i][j])]: return False
                if self.cols[j][int(board[i][j])]: return False
                sqn = (i//3)* 3 + (j//3)
                if self.sq[sqn][int(board[i][j])]: return False
                self.rows[i][int(board[i][j])] = True
                self.cols[j][int(board[i][j])] = True
                self.sq[sqn][int(board[i][j])] = True
        return True