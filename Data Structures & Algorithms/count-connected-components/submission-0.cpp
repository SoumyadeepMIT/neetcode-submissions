class Solution {
public:
    void dfs(vector<vector<int>>& adj, int u, vector<bool>& vis){
        if(vis[u]) return;
        vis[u] = true;
        for(int nei:adj[u]){
            dfs(adj, nei, vis);
        }
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<bool> vis(n, false);
        vector<vector<int>> adj(n);
        for(vector<int> e: edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        int res = 0;
        for(int i=0;i<n;i++){
            if(!vis[i]){
                res++;
                dfs(adj, i, vis);
            }
        }
        return res;
    }
};
