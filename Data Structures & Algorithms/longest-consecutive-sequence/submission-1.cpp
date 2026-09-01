class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> us(nums.begin(),nums.end());
        int res=0;
        for(int n:nums){
            if(us.find(n-1)==us.end()){
                int l = 1;
                while(us.find(n+l)!=us.end()){
                    l++;
                }
                res=max(res,l);
            }
        }
        return res;
    }
};
