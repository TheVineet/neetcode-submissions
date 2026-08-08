class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = []
        r1 = []
        lp=1
        rp=1
        l = 0
        for l in range(len(nums)):
            r = len(nums) - 1 - l
            left = nums[l]
            right = nums[r]
            l1.append(lp)
            r1.append(rp)
            lp *= left
            rp *= right
        r1.reverse()
        res = [l1[i] * r1[i] for i in range(len(nums))]

        return res
            
        
        # [1,1,2,8]
        # [1,6,24,48]
        # [48,24,12,8]
        # [1,1,2,8]
        # []


        