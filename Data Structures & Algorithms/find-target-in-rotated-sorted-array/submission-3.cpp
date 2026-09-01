class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0;
        int r=nums.size()-1;
        int res=-1;
        while(l<=r){
            int m = l+(r-l)/2;
            if(target==nums[m]){
                return m;
            }
            if(nums[m]>=nums[l]){
                if(target>nums[m]){
                    l=m+1;
                }
                else{
                    if(target<nums[l]){
                        l=m+1;
                    }
                    else{
                        r=m-1;
                    }
                }
            }
            else{
                if(target<nums[m]){
                    r=m-1;
                }
                else{
                    if(target>nums[r]){
                        r=m-1;
                    }
                    else{
                        l=m+1;
                    }
                }
            }
        }
        return -1;
    }
};
