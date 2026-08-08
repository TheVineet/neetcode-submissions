class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                curr = board[i][j]

                # check if it is .
                if curr == ".":
                    continue
                
                # check if the duplicate exists in that row
                if curr in rows[i]:
                    return False
                rows[i].add(curr)

                # check for column
                if curr in cols[j]:
                    return False
                cols[j].add(curr)

                # get current square index
                ind = ((i//3)*3 ) + (j // 3)
                # sq1 = i = 0,1,2,sq2, sq3
                # sq4 = i = 3,4,5, sq5,sq6
                # sq7 = i = 6,7,8, sq8, sq9

                if curr in sqrs[ind]:
                    return False
                sqrs[ind].add(curr)
        
        return True
                
        