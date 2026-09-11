class Solution {
public:
    int dfs(vector<vector<int>>& grid, vector<vector<bool>>& vis,int i, int j, int n, int m){
        if(i<0 || j<0 || i>=n || j>=m){
            return 0;
        }
        if(vis[i][j] || grid[i][j] == 0) return 0;
        vis[i][j] = true;
        return 1+dfs(grid, vis, i+1, j, n, m)+dfs(grid, vis, i, j+1, n, m)+dfs(grid, vis, i-1, j, n, m)+dfs(grid, vis, i, j-1, n, m);
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!vis[i][j] && grid[i][j] == 1){
                    res = max(res, dfs(grid, vis, i, j, n, m));
                }
            }
        }
        return res;
    }
};
