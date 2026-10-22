class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            if remaining < 0:
                return float("inf")
            
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1 + dfs(remaining - coin))
            memo[remaining] = res
            return res
        
        res = dfs(amount)
        return res if res != float("inf") else -1
