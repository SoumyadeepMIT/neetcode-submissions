class Solution {
public:
    bool isPalindrome(string s) {
        string res="";
        for(char c: s){
            if(isalpha(c)){
                res+=tolower(c);
            }
            else if(isdigit(c)){
                res+=c;
            }
            else{
                continue;
            }
        }
        int l=0;
        int r = res.size() -1;
        while(l<r){
            if(res[l]!=res[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};
