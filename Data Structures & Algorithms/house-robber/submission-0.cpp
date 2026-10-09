class Solution {
public:
    int cost(vector<int>& nums, int i, vector<int>& dp){
        if(i>=nums.size()) return 0;
        if(dp[i]!=-1) return dp[i];
        int p = cost(nums, i+2, dp) + nums[i];
        int np = cost(nums, i+1, dp);
        dp[i] = max(p, np);
        return dp[i];
    }
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return cost(nums, 0, dp);
    }
};
