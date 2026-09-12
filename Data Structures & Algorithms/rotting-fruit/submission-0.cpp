class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<pair<int,int>, int>> qu;
        vector<vector<int>> dir = {{1,0}, {-1, 0}, {0, 1}, {0,-1}};
        int fresh = 0;
        int res = 0;
        int n = grid.size();
        int m = grid[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 1) fresh++;
                else if(grid[i][j] == 2) qu.push({{i,j}, 0});
            }
        }
        while(!qu.empty()){
            int indx = qu.front().first.first;
            int indy = qu.front().first.second;
            int dis = qu.front().second;
            qu.pop();
            for(int i=0;i<4;i++){
                int x = indx + dir[i][0];
                int y = indy + dir[i][1];
                if(x<0 || y<0 || x>=n || y>=m || grid[x][y] == 0) continue;
                if(grid[x][y] == 1){
                    grid[x][y] = 2;
                    res = max(res,dis+1);
                    qu.push({{x,y},dis+1});
                    fresh--;
                }
            }
        }
        if(fresh!=0) return -1;
        return res;
    }
};
