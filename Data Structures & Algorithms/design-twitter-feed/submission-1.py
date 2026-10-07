class Twitter:

    def __init__(self):
        self.count = 0 #for time
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) #list of [count, tweetId]
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count = self.count -1 
        #Ideally it would be ++ but because we will be using negative
        # minHeap to implement max heap
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId) # Make user follow itself

        minHeap = []
        res = []
        
        #Get list of all tweets of followers
        for userId in self.followMap[userId]:
            tweets = self.tweetMap[userId]
            # now naturally, the latest tweet by that user would be at the end
            if tweets:
                index = len(tweets) - 1
                count,tweetId = tweets[index]
                minHeap.append([count,tweetId,userId,index])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            if minHeap:
                # heappop the latest, since counter is negative, so it would be the last one
                count,tweetId,userId,index = heapq.heappop(minHeap)
                res.append(tweetId)
                # now add the next index of that person in the minHeap
                index = index - 1
                tweets = self.tweetMap[userId]
                if index >= 0:
                    count,tweetId = tweets[index]
                    heapq.heappush(minHeap,[count,tweetId,userId,index])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
