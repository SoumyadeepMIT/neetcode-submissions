class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        sort(s1.begin(),s1.end());
        int l1 = s1.length();
        int l2 = s2.length();
        for(int i=0;i<=l2-l1;i++){
            string t = s2.substr(i,l1);
            sort(t.begin(), t.end());
            if(t == s1){
                return true;
            }
        }
        return false;
    }
};
