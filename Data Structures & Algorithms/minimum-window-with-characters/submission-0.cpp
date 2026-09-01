class Solution {
public:
    unordered_map<char,int> ums;
    unordered_map<char,int> umt;
    bool check(string t){
        for(char c:t){
            if(ums[c]<umt[c]){
                return false;
            }
        }
        return true;
    }
    string minWindow(string s, string t) {
        int l1 = s.length();
        int l2 = t.length();
        string res="";
        if(l2>l1){
            return res;
        }
        for(int i=0;i<l2;i++){
            umt[t[i]]++;
        }
        int l=0;
        int reslength=INT_MAX;
        for(int i=0;i<l1;i++){
            ums[s[i]]++;
            while(l<=i && check(t)){
                if(i-l+1<reslength){
                    res=s.substr(l,i-l+1);
                    reslength = i-l+1;
                }
                ums[s[l]]--;
                l++;
            }
        }
        return res;
    }
};
