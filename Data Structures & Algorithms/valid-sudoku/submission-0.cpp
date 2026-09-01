class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int,unordered_set<char>> row;
        unordered_map<int,unordered_set<char>> col;
        unordered_map<int,unordered_set<char>> sq;
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.'){
                    continue;
                }
                if(row[i].count(board[i][j]) || col[j].count(board[i][j]) || sq[3*(i/3)+j/3].count(board[i][j])){
                    return false;
                }
                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                sq[3*(i/3)+j/3].insert(board[i][j]);
            }
        }
        return true;
    }
};
