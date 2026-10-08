class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                row,col = q.popleft()
                directions = [[0,1],[1,0],[0,-1],[-1,0]]

                for dr,dc in directions:
                    r,c= row+dr, col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == 1:
                        area +=1
                        visit.add((r,c))
                        q.append((r,c))
            
            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea,area)
        
        return maxArea


