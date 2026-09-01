class Solution {
public:
    vector<vector<string>> res;
    void gen(string s, int i, vector<string> temp){
        if(i==s.length()){
            res.push_back(temp);
            return;
        }
        string ch="";
        for(int j=i;j<s.length();j++){
            ch+=s[j];
            string t = ch;
            reverse(t.begin(),t.end());
            if(t==ch){
                temp.push_back(ch);
                gen(s,j+1,temp);
                temp.pop_back();
            }
        }
        return;
    }
    vector<vector<string>> partition(string s) {
        gen(s,0,{});
        return res;
    }
};
