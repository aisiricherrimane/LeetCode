class Twitter:

    def __init__(self):
        self.followM = collections.defaultdict(set)
        self.tweet = collections.defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minH = []
        self.followM[userId].add(userId)

        for followerId in self.followM[userId]:
            if followerId in self.tweet:
                ind = len(self.tweet[followerId]) - 1
                time, tweetId = self.tweet[followerId][ind]
                heapq.heappush(minH, [time, tweetId, followerId, ind - 1])

        while minH and len(res) < 10:
            time, tweetId, followerId, ind = heapq.heappop(minH)
            res.append(tweetId)
            if ind >= 0:
                time, tweetId = self.tweet[followerId][ind]
                heapq.heappush(minH, [time, tweetId, followerId, ind - 1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId)  

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].remove(followeeId)
        if self.followM[followerId] == []:
            del self.followM[followerId]
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)