from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        lookup = {str(i) for i in range(1,27)}
        memo = {}
        # @cache
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            # Decode one digit
            ways = dfs(i + 1)

            # Decode two digit if valid
            if (i + 1) < len(s) and s[i:i+2] in lookup:
                ways += dfs(i + 2)
            
            memo[i] = ways
            return ways
            
        
        return dfs(0)
