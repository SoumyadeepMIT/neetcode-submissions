class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.dic = {}
        for s in strs:
            t = "".join(sorted(s))
            if t in self.dic:
                self.dic[t].append(s)
            else:
                self.dic[t] = [s]

        self.res = []
        for t in self.dic.keys():
            self.res.append(self.dic[t])
        return self.res
        