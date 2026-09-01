class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        i = 0
        n = len(path)
        while i<n:
            while i<n and path[i]=='/':
                i+=1
            dirname = ""
            while i<n and path[i]!='/':
                dirname+=path[i]
                i+=1
            if dirname == '..':
                if len(st)>0:st.pop()
            elif len(dirname)>0 and dirname != '.':
                st.append(dirname)
        if len(st) == 0:
            return "/"
        res = ""
        while len(st)!=0:
            res = "/" + st.pop() + res
        return res