class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap = []
        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            mheap.append([dist, p[0], p[1]])
        heapq.heapify(mheap)
        res = []
        while k!=0:
            dist, x, y = heapq.heappop(mheap)
            res.append([x,y])
            k-=1
        return res