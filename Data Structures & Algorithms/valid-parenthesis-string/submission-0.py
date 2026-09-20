class Solution:
    def checkValidString(self, s: str) -> bool:
        stl = []
        sts = []
        n = len(s)
        for i in range(n):
            if s[i]=='(':
                stl.append(i)
            elif s[i]=='*':
                sts.append(i)
            else:
                if len(stl)==0 and len(sts)==0:
                    return False
                elif len(stl)>0:
                    stl.pop()
                elif len(sts)>0:
                    sts.pop()
        while len(stl)>0:
            if len(sts)<=0:return False
            ind = sts[-1]
            if ind<stl[-1]:
                return False
            sts.pop()
            stl.pop()
        return True