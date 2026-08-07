class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ind = defaultdict(int)

        for n in nums:
            if ind[n] > 0:
                return True
            else:
                ind[n] += 1
        
        return False

        



