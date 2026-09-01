class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,bool> um;
        for(int n:nums){
            if(um.find(n)==um.end()){
                um[n]=true;
            }
            else{
                return true;
            }
        }
        return false;
    }
};
