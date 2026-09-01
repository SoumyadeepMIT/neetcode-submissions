class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskInd = [[t[0], t[1], i] for i, t in enumerate(tasks)]
        taskInd.sort(key = lambda x:x[0])
        ct = taskInd[0][0]
        res = []
        n = len(tasks)
        ind = 0
        pq = []
        while len(res)<n:
            if len(pq) == 0 and ind<n and ct<taskInd[ind][0]:
                ct = taskInd[ind][0]
            while ind<n and taskInd[ind][0]<=ct:
                heapq.heappush(pq, [taskInd[ind][1], taskInd[ind][2]])
                ind+=1
            if len(pq) == 0: continue
            pt, pind = heapq.heappop(pq)
            ct+=pt
            res.append(pind)
        return res            
