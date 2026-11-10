class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = set(nums)
        if len(nums) == len(lookup):
            return False
        else :
            return True

        
        