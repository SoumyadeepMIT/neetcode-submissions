class Solution {
public:
    int bins(vector<vector<int>>& tasks, int l, int r, int st){
        while(l<r){
            int m = (l+r+1)/2;
            if(tasks[m][1]<=st){
                l = m;
            }
            else{
                r = m - 1;
            }
        }
        return tasks[l][1]<=st ? l : -1;
    }
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<vector<int>> tasks;
        int n = startTime.size();
        for(int i=0;i<n;i++){
            tasks.push_back({startTime[i], endTime[i], profit[i]});
        }
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b){
            return a[1]<b[1];
        });
        vector<int> p;
        p.push_back(-1);
        for(int i=1;i<n;i++){
            int ind = bins(tasks, 0, i-1, tasks[i][0]);
            p.push_back(ind);
        }
        vector<int> dp(n,0);
        dp[0] = tasks[0][2];
        for(int i=1;i<n;i++){
            int ind = p[i];
            if(ind==-1){
                dp[i] = max(dp[i-1], tasks[i][2]);
            }
            else{
                dp[i] = max(dp[i-1], tasks[i][2] + dp[p[i]]);
            }
        }
        return dp[n-1];
    }
};