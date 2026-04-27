class Twitter:

    def __init__(self):
        self.tweets={}
        self.followees={}
        self.count=0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId not in self.tweets:
            self.tweets[userId]=[]
        heapq.heappush(self.tweets[userId],[-self.count,tweetId])
       
        

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        seen = set()

        
        people = [userId] + list(self.followees.get(userId, set()))

        for person in people:
            if person in self.tweets:
                for t in self.tweets[person]:
                    if t[1] not in seen:
                        heapq.heappush(all_tweets, t)
                        seen.add(t[1])

        result = []
        while all_tweets and len(result) < 10:
            result.append(heapq.heappop(all_tweets)[1])
        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = set()
        if followeeId not in self.followees[followerId]:
            self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].discard(followeeId)

        
