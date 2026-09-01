class Solution {
public:
    vector<vector<int>> res;
    void gen(vector<int>& nums, vector<int>& temp, int i){
        if(i==nums.size()){
            res.push_back(temp);
            return;
        }
        temp.push_back(nums[i]);
        gen(nums,temp,i+1);
        temp.pop_back();
        int j=i+1;
        while(j<nums.size() && nums[j]==nums[i]){
            j++;
        }
        gen(nums,temp,j);
        return;
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> temp;
        gen(nums,temp,0);
        return res;
    }
};
