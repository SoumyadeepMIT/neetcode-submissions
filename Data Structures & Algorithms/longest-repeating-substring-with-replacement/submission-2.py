class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        freq = [0 for _ in range(26)]
        res = 1
        mc = 0
        while r<n:
            freq[ord(s[r])-ord('A')] += 1
            mc = max(mc, freq[ord(s[r])-ord('A')])
            if (r-l+1-mc)>k:
                freq[ord(s[l]) - ord('A')]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
            