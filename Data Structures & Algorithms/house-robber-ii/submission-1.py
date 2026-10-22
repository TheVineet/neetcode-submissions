class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def getmax(nums):
            first,second = 0,0
            for i in range(len(nums)):
                curr = nums[i]
                temp = second
                second = max(curr + first, second)
                first = temp
            return second
        
        max1 = getmax(nums[:-1])
        max2 = getmax(nums[1:])

        return max(max1, max2)