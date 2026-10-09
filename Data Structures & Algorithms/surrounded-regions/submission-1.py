class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        q = collections.deque()
        nots = set()

        # scan the boundary rows and cols

        for c in range(cols):
            if board[0][c] == "O":
                q.append((0,c))
                nots.add((0,c))
            
            if board[rows-1][c] == "O":
                q.append((rows-1,c))
                nots.add((rows-1,c))
            
        
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r,0))
                nots.add((r,0))
            
            if board[r][cols-1] == "O":
                q.append((r,cols-1))
                nots.add((r,cols-1))

        # Find all nots that cant be captured
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    # check for out of bound
                    if r not in range(rows) or c not in range(cols) or (r,c) in nots or board[r][c] == "X" :
                        continue
                    
                    q.append((r,c))
                    nots.add((r,c))
        

        # capture remaining nots
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in nots:
                    board[r][c] = "X"
        



            
        