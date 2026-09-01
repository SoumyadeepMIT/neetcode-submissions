class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.pref = strs[0]
        for i in range(1, len(strs)):
            j=0
            while j < min(len(self.pref), len(strs[i])):
                if self.pref[j]!=strs[i][j]: break
                j+=1
            self.pref = self.pref[:j]
        return self.pref