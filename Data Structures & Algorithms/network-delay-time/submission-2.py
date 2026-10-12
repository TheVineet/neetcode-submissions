class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = collections.defaultdict(list)
        for v1,v2,d in times:
            adjMap[v1].append((d,v2))
        
        minHeap = [] #(t,v)
        visit = set()
        time = 0
        minHeap.append((0,k))

        while minHeap:
            t,v = heapq.heappop(minHeap)
            if v in visit:
                continue
            
            visit.add(v)

            for t1,v1 in adjMap[v]:
                heapq.heappush(minHeap, (t+t1,v1))
            
            time = max(t, time)
        
        return time if len(visit) ==n else -1


        