class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        res = 1
        l = 0
        r = 0
        n = len(s)
        let_check = {}
        while r<n:
            while l<r and (s[r] in let_check and let_check[s[r]]):
                let_check[s[l]] = False
                l+=1
            let_check[s[r]] = True
            res = max(res, r-l+1)
            r+=1
        return res