class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indeg(numCourses, 0);
        vector<vector<int>> adj(numCourses);
        for(vector<int> preq: prerequisites){
            adj[preq[1]].push_back(preq[0]);
            indeg[preq[0]]++;
        }
        queue<int> qu;
        vector<int> res;
        for(int i=0;i<numCourses;i++){
            if(indeg[i]==0)qu.push(i);
        }
        while(!qu.empty()){
            int n = qu.front();
            qu.pop();
            res.push_back(n);
            for(int nei:adj[n]){
                indeg[nei]--;
                if(indeg[nei]==0)qu.push(nei);
            }
        }
        if(res.size()!=numCourses) return {};
        return res;
    }
};
