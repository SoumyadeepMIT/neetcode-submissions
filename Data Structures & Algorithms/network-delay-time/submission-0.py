class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        dic = [[] for _ in range(n)]
        for u,v,t in times:
            dic[u-1].append((v-1, t))
        vis = [False] * n
        heapq.heappush(pq, (0, k-1))
        res = -1
        while len(pq)>0:
            w, u = heapq.heappop(pq)
            if vis[u]: continue
            vis[u] = True
            res = w
            for nei, wt in dic[u]:
                if not vis[nei]:
                    heapq.heappush(pq, (w+wt, nei))
        for i in range(n):
            if not vis[i]: return -1
        return res