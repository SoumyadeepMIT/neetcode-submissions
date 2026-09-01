class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        ns = ""
        for c in s:
            if c.isalnum():
                ns += c
        s = ns
        n = len(s)
        i = 0
        j = n-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True