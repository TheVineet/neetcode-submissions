import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            x = point[0]
            y = point[1]

            distance = x**2 + y**2

            heapq.heappush(maxHeap, (-distance, point))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for _, point in maxHeap]