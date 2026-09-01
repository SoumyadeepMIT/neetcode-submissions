class Solution {
public:
    int calcHours(vector<int>& piles, int s){
        int tot=0;
        for(int n:piles){
            tot+=(n+s-1)/s;
        }
        return tot;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = piles.size();
        int r=0;
        for(int i=0;i<n;i++){
            r=max(r,piles[i]);
        }
        int l=1;
        int res=-1;
        while(l<=r){
            int m=l+(r-l)/2;
            if(calcHours(piles,m)<=h){
                res=m;
                r=m-1;
            }
            else{
                l=m+1;
            }
        }
        return res;
    }
};
