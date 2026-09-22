import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        pq = []
        for i in intervals:
            heapq.heappush(pq,(i.start, 1))
            heapq.heappush(pq,(i.end, 0))
        c = 0
        res = 0
        while len(pq)>0:
            po, t = heapq.heappop(pq)
            if t==1:
                c+=1
                res = max(res, c)
            else:
                c-=1
        return res