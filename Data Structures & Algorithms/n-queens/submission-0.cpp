class Solution {
public:
    vector<vector<string>> res;
    bool isValid(int i,int j,vector<string>& dp,int n){
        int r = i;
        int c = j;
        while(r>=0){
            if(dp[r][c]=='Q'){
                return false;
            }
            r--;
        }
        r=i;
        while(r>=0 && c>=0){
            if(dp[r][c]=='Q'){
                return false;
            }
            r--;
            c--;
        }
        r=i;
        c=j;
        while(r>=0 && c<n){
            if(dp[r][c]=='Q'){
                return false;
            }
            r--;
            c++;
        }
        return true;
    }
    void gen(int n, vector<string>& dp,int i){
        if(i==n){
            res.push_back(dp);
            return;
        }
        for(int j=0;j<n;j++){
            if(isValid(i,j,dp,n)){
                dp[i][j]='Q';
                gen(n,dp,i+1);
                dp[i][j]='.';
            }
        }
        return;
    }
    vector<vector<string>> solveNQueens(int n) {
        string s="";
        for(int i=0;i<n;i++){
            s+='.';
        }
        vector<string> dp(n,s);
        gen(n,dp,0);
        return res;
    }
};
