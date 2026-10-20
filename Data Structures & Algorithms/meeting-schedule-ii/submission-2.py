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
        intervals.sort(key = lambda x:x.start)
        for i in intervals:
            st, end = i.start, i.end
            if len(pq)>0:
                if st<pq[0]:
                    heapq.heappush(pq, end)
                else:
                    heapq.heappop(pq)
                    heapq.heappush(pq, end)
            else:
                heapq.heappush(pq, end)
        return len(pq)
            