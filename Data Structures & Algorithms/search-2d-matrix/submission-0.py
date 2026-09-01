class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rows in matrix:
            l = 0
            r = len(rows) - 1
            while l <= r:
                m = l + (r-l)//2
                if target > rows[m]:
                    l = m + 1
                elif target < rows[m]:
                    r = m - 1
                else:
                    return True
            continue

        return False