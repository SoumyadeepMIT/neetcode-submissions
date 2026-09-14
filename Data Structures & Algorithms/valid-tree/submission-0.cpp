class Solution {
public:
    bool checkCycle(int n, vector<vector<int>>& adj, vector<bool>& vis, int u, int p){
        if(vis[u]) return false;
        vis[u] = true;
        for(int nei: adj[u]){
            if(vis[nei] && nei!=p){
                return true;
            }
            if(checkCycle(n, adj, vis, nei, u))
                return true;
        }
        return false;
    }
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<bool> vis(n, false);
        vector<vector<int>> adj(n);
        for(vector<int> e: edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        if(checkCycle(n, adj, vis, 0, -1))
            return false;
            
        for(int i=0;i<n;i++){
            if(!vis[i]) return false;
        }
        return true;
    }
};
