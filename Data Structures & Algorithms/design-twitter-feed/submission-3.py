class Twitter:

    def __init__(self):
        self.tweets={}
        self.followees={}
        self.count=0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append((-self.count, tweetId))
       
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        heap=[]
        
        people = set([userId]) | self.followees.get(userId, set())


        for person in people:
            if person in self.tweets:
                time,tweetId=self.tweets[person][-1]
                heapq.heappush(heap,(time,tweetId,person,len(self.tweets[person])-1))
        while heap and len(result)<10:
            time,tweetId,person,idx=heapq.heappop(heap)
            result.append(tweetId)
            if idx-1>=0:
                prev_time,prev_tweet=self.tweets[person][idx-1]
                heapq.heappush(heap,(prev_time,prev_tweet,person,idx-1))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = set()
        if followeeId not in self.followees[followerId]:
            self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].discard(followeeId)

        
