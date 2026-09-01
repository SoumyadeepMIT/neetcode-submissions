class Solution {
public:
    bool isValid(int i,int j,int r,int c){
        if(i<0 || j<0 || i>=r || j>=c){
            return false;
        }
        return true;
    }
    bool dfs(vector<vector<char>>& board, string word, int i,int j,int wi, vector<vector<bool>>& vis){
        if(!isValid(i,j,board.size(),board[0].size())){
            return false;
        }
        if(vis[i][j]){
            return false;
        }
        if(wi==word.size()-1 && board[i][j]==word[wi]){
            return true;
        }
        if(board[i][j]!=word[wi]){
            return false;
        }
        vis[i][j]=true;
        bool a = dfs(board,word,i+1,j,wi+1, vis);
        bool b = dfs(board,word,i,j+1,wi+1, vis);
        bool c = dfs(board,word,i-1,j,wi+1, vis);
        bool d = dfs(board,word,i,j-1,wi+1, vis);
        vis[i][j]=false;
        return a || b || c || d;
        
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;

        for(string word:words){
            bool f = false;
            for(int i=0;i<board.size();i++){
                for(int j=0;j<board[0].size();j++){
                    if(board[i][j]==word[0]){
                        vector<vector<bool>> vis(board.size(), vector<bool>(board[0].size(), false));
                        if(dfs(board, word, i, j, 0, vis)){
                            f=true;
                            res.push_back(word);
                            break;
                        }
                    }
                }
                if(f){
                    break;
                }
            }
        }
        return res;
    }
};
