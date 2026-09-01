class Solution {
public:
    vector<string> res;
    void gen(string digits, int i,string s, vector<string>& dp){
        if(i==digits.length()){
            if(s.length()==0){
                return;
            }
            res.push_back(s);
            return;
        }
        int ind = int(digits[i]-'0');
        for(int j=0;j<dp[ind].length();j++){
            gen(digits,i+1,s+dp[ind][j],dp);
        }
        return;
    }
    vector<string> letterCombinations(string digits) {
        vector<string> dp = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        gen(digits,0,"",dp);
        return res;
    }
};
