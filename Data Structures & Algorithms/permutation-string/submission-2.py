class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        i = 0
        s1 = "".join(sorted(s1))
        while i+k<=len(s2):
            sp = s2[i:i+k]
            sp = "".join(sorted(sp))
            if sp == s1: return True
            i+=1
        return False

    
