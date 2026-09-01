class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for c in tasks:
            ind = ord(c[0]) - ord('A')
            freq[ind] += 1
        mheap = []
        for i in range(26):
            if freq[i]>0:
                heapq.heappush(mheap, [-freq[i], i])
        t = 0
        qu = deque()
        while not (len(mheap) == 0 and len(qu) == 0):
            t+=1
            while len(qu)>0 and t>=qu[0][1]:
                heapq.heappush(mheap, [-freq[qu[0][0]], qu[0][0]])
                qu.popleft()
            if len(mheap)>0:
                f, ind = heapq.heappop(mheap)
                freq[ind] -= 1
                if freq[ind]>0:
                    qu.append([ind, t+n+1])
        return t