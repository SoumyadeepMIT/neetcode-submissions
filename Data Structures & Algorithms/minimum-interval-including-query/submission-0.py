class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ev = []
        for i, (st, end) in enumerate(intervals):
            ev.append((st, 0, end-st+1, i))
            ev.append((end, 2, end-st+1, i))
        for i, q in enumerate(queries):
            ev.append((q, 1, i))
        ev.sort(key = lambda x: (x[0], x[1]))
        inact = [False] * len(intervals)
        res = [-1] * len(queries)
        hp = []
        for ind, typ, *rest in ev:
            if typ == 0:
                sz, idx = rest
                heapq.heappush(hp, (sz, idx))
            elif typ == 2:
                sz, idx = rest
                inact[idx] = True
            else:
                while hp and inact[hp[0][1]]:
                    heapq.heappop(hp)
                if hp:
                    res[rest[0]] = hp[0][0]
        return res