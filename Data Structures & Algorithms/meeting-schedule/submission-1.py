"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        n = len(intervals)
        if n==0:return True
        e = intervals[0].end
        for i in range(1, n):
            if intervals[i].start<e:
                return False
            else:
                e = intervals[i].end
        return True