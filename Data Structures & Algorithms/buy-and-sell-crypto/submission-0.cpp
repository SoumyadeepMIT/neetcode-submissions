class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res=0;
        int n = prices.size();
        int m = prices[n-1];
        for(int i=n-2;i>=0;i--){
            m=max(prices[i],m);
            res=max(res,m-prices[i]);
        }
        return res;
    }
};
