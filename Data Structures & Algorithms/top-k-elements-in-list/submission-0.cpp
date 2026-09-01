class Solution {
public:

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        int n = nums.size();
        vector<vector<int>> f(n+1);
        for(int num:nums){
            count[num]++;
        }
        for(auto it: count){
            f[it.second].push_back(it.first);
        }
        vector<int> res;
        int c=0;
        for(int i=n;i>=0;i--){
            for(int j:f[i]){
                res.push_back(j);
                c++;
                if(c==k){
                    return res;
                }
            }
        }
        return res;
    }
};
