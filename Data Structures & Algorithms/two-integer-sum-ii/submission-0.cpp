class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int r=numbers.size()-1;
        int l=0;
        vector<int> res;
        while(l<r){
            if(numbers[l]+numbers[r]==target){
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            }
            else if(numbers[l]+numbers[r]<target){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
};
