class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        e = intervals[0][1]
        s = intervals[0][0]
        n = len(intervals)
        if n==1:
            return intervals
        i=0
        while i<n:
            if intervals[i][0]<=e:
                e = max(e, intervals[i][1])
                s = min(s,intervals[i][0])
            else:
                res.append([s,e])
                e = intervals[i][1]
                s = intervals[i][0]
            i+=1
        res.append([s,e])
        return res