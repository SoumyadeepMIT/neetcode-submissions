class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<pair<int,int>,int>> qu;
        vector<vector<int>> dir = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 0){
                    vis[i][j] = true;
                    qu.push({{i,j}, 0});
                }
            }
        }
        while(!qu.empty()){
            int indi = qu.front().first.first;
            int indj = qu.front().first.second;
            int dis = qu.front().second;
            qu.pop();
            for(int i=0;i<4;i++){
                int x = indi+dir[i][0];
                int y = indj + dir[i][1];
                if(x<0 || y<0 || x>=n || y>=m || vis[x][y] || grid[x][y] == -1) continue;
                grid[x][y] = dis+1;
                vis[x][y] = true;
                qu.push({{x,y}, dis+1});
            }
        }

    }
};
