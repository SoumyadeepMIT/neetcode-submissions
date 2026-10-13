class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))
        res = []
        res.append(-pq[0][0])
        for i in range(k, n):
            heapq.heappush(pq, (-nums[i], i))
            while len(pq)>0 and pq[0][1]<=(i-k):
                heapq.heappop(pq)
            res.append(-pq[0][0])
        return res