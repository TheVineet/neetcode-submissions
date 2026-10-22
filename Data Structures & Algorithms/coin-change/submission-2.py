class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            minC = float("inf")
            for coin in coins:
                if i >= coin:
                    minC = min(minC, 1 + dp[i - coin])
            dp[i] = minC
        
        return dp[amount] if dp[amount] != float("inf") else -1
            
