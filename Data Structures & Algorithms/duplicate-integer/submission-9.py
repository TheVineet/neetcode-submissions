class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for i in nums:
            lookup.add(i)
        
        if len(nums) == len(lookup):
            return False
        else :
            return True

        
        