class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        ls = self.dic[key]
        l = 0
        r = len(ls)-1
        res = ""
        while l<=r:
            m = l+(r-l)//2
            if ls[m][0]<=timestamp:
                res = ls[m][1]
                l=m+1
            else:
                r = m-1
        return res

