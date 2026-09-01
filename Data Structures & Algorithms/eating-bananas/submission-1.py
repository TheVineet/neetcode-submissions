class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)

        i = 1
        j = max_rate
        k = max_rate

        while i <= j:
            m = i + (j-i)//2
            t_h = 0
            for pile in piles:
                t_h = t_h + (pile + m - 1)//m
            if h >= t_h:
                j = m - 1
                k = min(k,m)
            elif h < t_h:
                i = m + 1
                
        return k



        