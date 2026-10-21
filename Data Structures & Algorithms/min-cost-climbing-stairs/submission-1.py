class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one,two = cost[-1],0
        j = len(cost) - 2

        for i in range(len(cost) - 1):
            currCost = cost[j]
            temp = one
            one = currCost + min(one,two)
            two = temp
            j -= 1
        
        return min(one,two)
            
        
        