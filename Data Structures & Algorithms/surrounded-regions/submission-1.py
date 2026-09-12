class Solution:
    def dfs(self, board, i, j, m, n):
        if i<0 or j<0 or i>=m or j>=n: return
        if board[i][j] == '#' or board[i][j] == 'X':
            return
        board[i][j] = '#'
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            self.dfs(board, x, y, m, n)

    def solve(self, board: List[List[str]]) -> None:
        self.dir = [[1,0],[-1,0],[0,1],[0,-1]]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, m, n)
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1, m, n)
        for i in range(n):
            if board[0][i] == 'O':
                self.dfs(board, 0, i, m, n)
            if board[m-1][i] == 'O':
                self.dfs(board, m-1, i, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '#': board[i][j] = 'O'
            