class Solution {
public:
    vector<vector<int>> res;
    void gen(vector<int>& nums, int target, int sum,int i, vector<int>& temp){
        if(sum==target){
            res.push_back(temp);
            return;
        }
        if(sum>target){
            return;
        }
        for(int j=i;j<nums.size();j++){
            temp.push_back(nums[j]);
            gen(nums,target,sum+nums[j],j,temp);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> temp;
        gen(nums, target, 0, 0, temp);
        
        return res;
    }
};
