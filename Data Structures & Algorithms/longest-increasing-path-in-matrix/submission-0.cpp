class Solution {
public:
    int dfs(int i, int j, int r, int c, vector<vector<int>>& matrix, vector<vector<int>>& dp, int pm){
        if(i<0 || j<0 || i>=r || j>=c || matrix[i][j]<=pm) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        int res = 1;
        res = max(res, 1+dfs(i+1, j, r, c, matrix, dp, matrix[i][j]));
        res = max(res, 1+dfs(i-1, j, r, c, matrix, dp, matrix[i][j]));
        res = max(res, 1+dfs(i, j+1, r, c, matrix, dp, matrix[i][j]));
        res = max(res, 1+dfs(i, j-1, r, c, matrix, dp, matrix[i][j]));
        dp[i][j] = res;
        return res;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int r = matrix.size();
        int c = matrix[0].size();
        vector<vector<int>> dp(r, vector<int>(c, -1));
        int res = 1;
        for(int i = 0;i<r;i++){
            for(int j = 0; j<c; j++){
                res = max(res, dfs(i, j, r, c, matrix, dp, INT_MIN));
            }
        }
        return res;
    }
};
