class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        res = 0

        l = 0
        r = len(height) - 1

        while l < r:
            left = height[l]
            right = height[r]

            maxLeft = max(left, maxLeft)
            maxRight = max(right, maxRight)

            min1 = min(maxLeft,maxRight)

            if maxLeft == min1:
                area = maxLeft - height[l]
                l +=1
            
            else :
                area = maxRight - height[r]
                r -=1
            res +=area
        return res
