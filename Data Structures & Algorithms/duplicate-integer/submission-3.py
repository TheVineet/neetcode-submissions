class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ind = set()

        for n in nums:
            if n in ind:
                return True
            else:
                ind.add(n)
        
        return False
        