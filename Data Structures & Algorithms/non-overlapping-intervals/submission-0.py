class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        maxIntervals = 0
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        l = 1
        e = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<e: continue
            else:
                l+=1
                e = intervals[i][1]
        return n-l