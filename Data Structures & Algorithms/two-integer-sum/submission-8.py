class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if indices.get(compliment) != None:
                return [min(i, indices[compliment]),max(i, indices[compliment])]
            else:
                indices[nums[i]] = i
             

        