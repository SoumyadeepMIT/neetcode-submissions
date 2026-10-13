class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n>m: return False
        freq = [0] * 26
        sfreq = [0] * 26
        for i in range(n):
            freq[ord(s2[i])-ord('a')] += 1
            sfreq[ord(s1[i]) - ord('a')]+=1
        if freq == sfreq: return True
        l = 0
        r = n
        while r<m:
            freq[ord(s2[l])-ord('a')]-=1
            freq[ord(s2[r])-ord('a')]+=1
            for i in range(26):
                if freq==sfreq: return True
            l+=1
            r+=1
        return False