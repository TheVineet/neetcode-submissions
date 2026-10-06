class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We need maxHeap. but python doest provide max heap. 
        # So we will use negative values to make it act like max heap.

        s = [-s for s in stones]

        heapq.heapify(s)

        while len(s) > 1:
            first = abs(heapq.heappop(s))
            second = abs(heapq.heappop(s))

            if first > second :
                heapq.heappush(s, -(first - second))
        
        # if heap was empty
        heapq.heappush(s,0)

        return abs(heapq.heappop(s))



        