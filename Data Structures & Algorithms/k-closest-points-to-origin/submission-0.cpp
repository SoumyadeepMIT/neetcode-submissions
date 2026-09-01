class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double,pair<int,int>>, vector<pair<double,pair<int,int>>>, greater<pair<double,pair<int,int>>>> pq;
        for(vector<int> p:points){
            double d = sqrt((double)(p[0]*p[0]) + (double)(p[1]*p[1]));
            pq.push({d,{p[0],p[1]}});
        }
        vector<vector<int>> res(k);
        int i=0;
        while(k>0){
            pair<double,pair<int,int>> p = pq.top();
            pq.pop();
            res[i].push_back(p.second.first);
            res[i++].push_back(p.second.second);
            k--;
        }
        return res;
    }
};
