class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posD = set() # r + c
        negD = set() # r - c

        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r >= n:
                copy = ["".join(r) for r in board]
                res.append(copy)
            
            for c in range(n):
                if c in col or (r + c) in posD or (r-c) in negD:
                    continue
                
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = "."
        
        dfs(0)
        return res

