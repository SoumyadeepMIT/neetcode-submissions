class Solution {
public:
    vector<vector<int>> res;
    void gen(vector<int>& nums, int target, int i, int sum,vector<int>& temp){
        if(sum==target){
            res.push_back(temp);
            return;
        }
        if(sum>target)
            return;
        for(int j=i;j<nums.size();j++){
            temp.push_back(nums[j]);
            gen(nums,target,j+1,sum+nums[j], temp);
            temp.pop_back();
            while(j<nums.size()-1 && nums[j+1]==nums[j]){
                j++;
            }
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> temp;
        sort(candidates.begin(), candidates.end());
        gen(candidates,target,0,0,temp);
        return res;
    }
};
