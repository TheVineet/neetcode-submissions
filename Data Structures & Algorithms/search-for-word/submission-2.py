class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])

        def dfs(r,c,i, path):
            if len(path) == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or len(path) > len(word) or board[r][c] != word[i] or (r,c) in path:
                return
            
            path.add((r,c))

            # consider all 4 adjacent directions
            if dfs(r + 1,c,i+1,path) :
                return True
            if dfs(r - 1,c,i+1,path) :
                return True
            if dfs(r,c + 1,i+1,path) :
                return True
            if dfs(r,c -1,i+1,path) :
                return True
            
            path.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0,set()):
                    return True
        

        return False

        

        

            