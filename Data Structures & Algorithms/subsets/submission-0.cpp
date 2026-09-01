class Solution {
public:
    vector<vector<int>> res;
    void gen(vector<int>& nums, int i, vector<int>& temp){
        if(i==nums.size()){
            res.push_back(temp);
            return;
        }
        temp.push_back(nums[i]);
        gen(nums,i+1,temp);
        temp.pop_back();
        gen(nums,i+1,temp);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        gen(nums,0,temp);
        return res;
    }
};
