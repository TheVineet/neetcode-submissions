from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        lookup = {str(i) for i in range(1,27)}
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0

            # Decode one digit
            ways = dfs(i + 1)

            # Decode two digit if valid
            if (i + 1) < len(s) and s[i:i+2] in lookup:
                ways += dfs(i + 2)
            
            return ways
            
        
        return dfs(0)
