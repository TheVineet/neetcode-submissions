class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        lp=1
        rp=1
        for i in range(len(nums)):
            r = len(nums)-i-1
            res[i] = res[i] * lp
            res[r] = res[r] * rp
            lp = lp * nums[i]
            rp = rp * nums[r]
        
        return res
             
