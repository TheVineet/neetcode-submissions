class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visit or grid[r][c] != 1:
                        continue
                    
                    visit.add((r,c))
                    q.append((r,c))
                    area +=1
            
            return area
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea




        