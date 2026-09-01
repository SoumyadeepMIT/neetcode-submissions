class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left(n,-1);
        vector<int> right(n,-1);
        left[0]=height[0];
        for(int i=1;i<n;i++){
            left[i]=max(left[i-1],height[i]);
        }
        right[n-1]=height[n-1];
        for(int i=n-2;i>=0;i--){
            right[i]=max(right[i+1],height[i]);
        }
        int res=0;
        for(int i=1;i<n-1;i++){
            int m = min(left[i-1],right[i+1]);
            if(m>height[i]){
                res+=(m-height[i]);
            }
        }
        return res;
    }
};
