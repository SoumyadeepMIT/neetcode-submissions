class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> um;
        for(string s:strs){
            string t=s;
            sort(t.begin(),t.end());
            um[t].push_back(s);
        }
        vector<vector<string>> res;
        for(auto it:um){
            res.push_back(it.second);
        }
        return res;
    }
};
