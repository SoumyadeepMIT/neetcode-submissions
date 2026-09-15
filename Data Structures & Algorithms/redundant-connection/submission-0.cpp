class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> deg(n+1, 0);
        queue<int> qu;
        vector<vector<int>> adj(n+1);
        for(vector<int> e:edges){
            deg[e[0]]++;
            deg[e[1]]++;
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        for(int i=1;i<=n;i++){
            if(deg[i]==1) qu.push(i);
        }
        while(!qu.empty()){
            int nod = qu.front();
            deg[nod]--;
            qu.pop();
            for(int nei: adj[nod]){
                deg[nei]--;
                if(deg[nei]==1){
                    qu.push(nei);
                }
            }
        }
        for(int i=n-1;i>=0;i--){
            if(deg[edges[i][0]]==2 && deg[edges[i][1]]>0){
                return edges[i];
            }
        }
        return {};
    }
};
