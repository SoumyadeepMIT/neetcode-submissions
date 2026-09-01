class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res=0;
        int n = s.length();
        unordered_map<char,int> freq;
        int l=0;
        int r=0;
        while(l<n){
            freq[s[l]]++;
            while(r<=l && freq[s[l]]>1){
                freq[s[r]]--;
                r++;
            }
            res=max(res,l-r+1);
            l++;
        }
        return res;
    }
};
