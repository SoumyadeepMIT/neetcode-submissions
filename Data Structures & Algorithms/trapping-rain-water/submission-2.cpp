class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left(n,0);
        vector<int> right(n,0);
        int res = 0;
        int maxl = height[0];
        for(int i=1;i<n;i++){
            left[i] = maxl;
            maxl = max(maxl,height[i]);
        }
        int maxr = height[n-1];
        for(int i=n-2;i>=0;i--){
            right[i] = maxr;
            maxr = max(maxr,height[i]);
        }
        for(int i=1;i<n-1;i++){
            int m = min(left[i],right[i]) - height[i];
            if(m>0) res+=m;
        }
        return res;
    }
};
