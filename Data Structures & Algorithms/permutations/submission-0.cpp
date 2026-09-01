class Solution {
public:
    vector<vector<int>> res;
    void gen(vector<int>& nums, vector<int>& temp, vector<bool>& vis){
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }
        for(int j=0;j<nums.size();j++){
            if(vis[j]){
                continue;
            }
            temp.push_back(nums[j]);
            vis[j]=true;
            gen(nums,temp,vis);
            temp.pop_back();
            vis[j]=false;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        vector<bool> vis(nums.size(), false);
        gen(nums, temp, vis);
        return res;
    }
};
