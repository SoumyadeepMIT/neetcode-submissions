class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> um;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            int sec = target-nums[i];
            if(um.find(sec)!=um.end()){
                res.push_back(um[sec]);
                res.push_back(i);
                return res;
            }
            else{
                um[nums[i]]=i;
            }
        }
        return res;
    }
};
