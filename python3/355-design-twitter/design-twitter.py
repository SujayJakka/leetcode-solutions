import heapq

class Twitter:

    def __init__(self):
        self.follower_to_followee = {}
        self.user_to_post = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time -= 1

        if userId not in self.user_to_post:
            self.user_to_post[userId] = [(self.time, tweetId)]
            self.follower_to_followee[userId] = {userId}
        else:
            self.user_to_post[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        res = []

        if userId not in self.user_to_post:
            return

        for follower in self.follower_to_followee[userId]:
            arr.extend(self.user_to_post[follower])
        
        heapify(arr)

        i = 0
        while arr and i < 10:
            recent_post = heappop(arr)
            res.append(recent_post)
            i += 1
        
        return [y for x, y in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_to_followee:
            self.follower_to_followee[followerId] = {followerId}
            self.user_to_post[followerId] = []
        
        if followeeId not in self.follower_to_followee:
            self.follower_to_followee[followeeId] = {followeeId}
            self.user_to_post[followeeId] = []

        self.follower_to_followee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.follower_to_followee[followerId]:
            self.follower_to_followee[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)