class Solution {
public:

    string encode(vector<string>& strs) {
        string s="";
        for(string st:strs){
            s+=to_string(st.size())+"#"+st;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> res;
        for(int i=0;i<s.length();i++){
            int j=i;
            while(s[j]!='#'){
                j++;
            }
            int l=stoi(s.substr(i,j-i));
            string str = s.substr(j+1,l);
            res.push_back(str);
            i=j+l;
        }
        return res;
    }
};
