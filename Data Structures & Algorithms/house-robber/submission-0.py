class Solution:
    def rob(self, nums: List[int]) -> int:
        first,second = 0,0
        for i in range(len(nums)):
            curr = nums[i]
            temp = second
            second = max(first + curr, second)
            first = temp
        return second