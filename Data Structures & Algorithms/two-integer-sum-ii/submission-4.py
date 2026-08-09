class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            left = numbers[l]
            right = numbers[r]
            sum = left + right
            if sum == target:
                return [l + 1,r + 1]
            
            if sum > target:
                r = r -1
            if sum < target :
                l = l + 1
            
        