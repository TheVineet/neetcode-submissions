class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pac = set()
        atlantic = set()

        def dfs(r,c,visit, prevHeight):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))
            # call dfs for all its neighbours
            dfs(r + 1,c,visit,heights[r][c])
            dfs(r - 1,c,visit,heights[r][c])
            dfs(r,c + 1,visit,heights[r][c])
            dfs(r,c - 1,visit,heights[r][c])
        

        # Now addling the topmost and bottomost row
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows - 1,c,atlantic,heights[rows - 1][c])
        
        # for the side columns
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        
        res = []
        # Finding the common
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atlantic:
                    res.append([r,c])

        return res

        