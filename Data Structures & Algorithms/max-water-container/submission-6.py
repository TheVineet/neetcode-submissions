class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            left = heights[l]
            right = heights[r]
            width = r - l
            minL = min(left, right)
            area = width * minL
            maxArea = max(maxArea, area)
            
            if minL == right:
                r -=1
            else :
                l +=1
        
        return maxArea
        