class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Core Logic:
        1. Count the occurence of each letter.
        2. create a minHeap with the - values of the counts.
        3. Initialise a q, to store [count, time] where count is the value popped
        from the heap time is the time when it would
        be pushed back in the queue. 
        4. check if current time matches the time of the left element of queue.
        5. If it does, push it into the heap.
        """

        count = Counter(tasks)
        minHeap = [-cnt for cnt in count.values()]
        heapq.heapify(minHeap)

        time = 0
        q = deque()

        while minHeap or q:
            time +=1
            if minHeap:   
                cnt = abs(heapq.heappop(minHeap)) - 1
                if cnt > 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(minHeap, -(q.popleft()[0]))
        
        return time
            

        