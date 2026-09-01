class Solution {
public:
    vector<string> res;
    void gen(int o,int c,int n,string cur){
        if(o==n && o==c){
            res.push_back(cur);
            return;
        }
        if(o<n)
            gen(o+1,c,n,cur+'(');
        if(c<o){
            gen(o,c+1,n,cur+')');
        }
    }
    vector<string> generateParenthesis(int n) {
        gen(0,0,n,"");
        return res;
    }
};
