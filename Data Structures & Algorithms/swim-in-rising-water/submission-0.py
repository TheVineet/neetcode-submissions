class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        minHeap = [] #t, r,c
        visit = set() #r,c

        heapq.heappush(minHeap,(grid[0][0], 0, 0))
        visit.add((0,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if r == rows-1 and c == cols - 1:
                    return t

            for dr,dc in directions:
                row , col = r + dr, c + dc
                # check for out of bound
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if (row,col) not in visit:
                    visit.add((row,col))
                    heapq.heappush(minHeap, (max(t,grid[row][col]),row,col))
        

                
                
                



        