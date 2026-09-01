class Twitter:

    def __init__(self):
        self.count = 0
        self.fmap = {}
        self.tmap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tmap:
            self.tmap[userId] =  [(self.count, tweetId)]
            return
        self.tmap[userId].append((self.count, tweetId))       

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        if userId in self.tmap:
            for c, tid in self.tmap[userId]:
                heapq.heappush(pq, [c, tid])
                if len(pq)>10:
                    heapq.heappop(pq)
        if userId in self.fmap:
            for fid in self.fmap[userId]:
                if fid not in self.tmap: continue
                for c, tid in self.tmap[fid]:
                    heapq.heappush(pq, [c, tid])
                    if len(pq)>10:
                        heapq.heappop(pq)
        res = []
        while len(pq)>0:
            c, tid = heapq.heappop(pq)
            res.append(tid)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.fmap:
            self.fmap[followerId] = [followeeId]
            return
        if followeeId in self.fmap[followerId]: return
        self.fmap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.fmap: return
        if followeeId not in self.fmap[followerId]: return
        self.fmap[followerId].remove(followeeId)
