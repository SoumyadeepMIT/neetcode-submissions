class Solution {
public:
    int dfs(vector<vector<int>>& grid,int i, int j, int n, int m){
        if(i<0 || j<0 || i>=n || j>=m){
            return 0;
        }
        if(grid[i][j] == 0) return 0;
        grid[i][j] = 0;
        return 1+dfs(grid, i+1, j, n, m)+dfs(grid, i, j+1, n, m)+dfs(grid, i-1, j, n, m)+dfs(grid,i, j-1, n, m);
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 1){
                    res = max(res, dfs(grid, i, j, n, m));
                }
            }
        }
        return res;
    }
};
