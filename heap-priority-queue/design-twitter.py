
class Twitter:
    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time, tweetId])
        self.time -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followmap[userId].add(userId)
        
        for following in self.followmap[userId]:
            if following in self.tweetmap:
                ind = len(self.tweetmap[following]) - 1
                time, tweetId = self.tweetmap[following][ind]
                heapq.heappush(minheap,[time, tweetId, following, ind - 1])
        
        while minheap and len(res) < 10:
            time, tweetId, following, ind = heapq.heappop(minheap)
            res.append(tweetId)
            if ind >= 0:
                heapq.heappush(minheap,[time, self.tweetMap[following][ind][1], self.tweetMap[following][ind][0], ind - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap or followeeId not in self.followmap[followerId]:
            return 
        self.followmap[followerId].remove(followeeId)
        if not self.followmap[followerId]:
            del self.followmap[followerId]



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)