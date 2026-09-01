class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res = res + "#" + str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                l = ""
                i+=1
                while s[i] != '#':
                    l += s[i]
                    i+=1
                l = int(l)
                st = ""
                i+=1
                j = 0
                for j in range(l):
                    st += s[i]
                    i+=1
                res.append(st)
        return res