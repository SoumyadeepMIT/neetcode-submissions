from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        n = len(s)
        for i in range(n):
            freq[s[i]] = i
        res = []
        l = 1
        maxi = freq[s[0]]
        for i in range(1,n):
            if i>maxi:
                res.append(l)
                l = 1
            else:
                l+=1
            maxi = max(maxi, freq[s[i]])
        res.append(l)
        return res