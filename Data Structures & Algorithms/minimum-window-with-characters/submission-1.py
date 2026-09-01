class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        
        dic_t = {}
        for c in t:
            dic_t[c] = dic_t.get(c, 0) + 1
        
        dic_s = {}
        l = 0
        res = ""
        reslen = len(s) + 1
        
        def check():
            for char in dic_t.keys():
                if dic_s.get(char, 0) < dic_t[char]:  # At least, not exact
                    return False
            return True
        
        for r in range(len(s)):
            dic_s[s[r]] = dic_s.get(s[r], 0) + 1
            
            while check():  # Removed l<r condition
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]  # Slice s, not dic_s
                dic_s[s[l]] -= 1
                l += 1
        
        return res