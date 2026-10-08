class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True #We want to break
            
            if r < 0 or c < 0 or r >= ROW or c >= COL or word[i] != board[r][c] or (r,c) in path:
                return False
        

            path.add((r,c)) #Consider current
            # Check in all four directions

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            path.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                found = dfs(r,c,0)
                if found :
                   return True

        return False

        