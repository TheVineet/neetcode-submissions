class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjMap = {i:[] for i in range(len(points))} #Cost,point

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i +1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjMap[i].append((dist,j))
                adjMap[j].append((dist,i))
        
        minHeap = [(0,0)] #(cost,point)
        visit = set() #point
        res = 0 #Cost

        while len(visit) < len(points):
            cost,point = heapq.heappop(minHeap)
            if point in visit:
                continue
            
            visit.add(point)
            res += cost

            for c,p in adjMap[point]:
                if p not in visit:
                    heapq.heappush(minHeap,(c,p))
        
        return res

            