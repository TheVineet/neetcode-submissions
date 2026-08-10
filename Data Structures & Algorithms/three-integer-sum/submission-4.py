class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for k in range(len(nums) - 2):
            t = nums[k]
            if k > 0 and nums[k] == nums[k -1]:
                continue  
        
            l = k + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[k] + nums[l] + nums[r]

                if sum < 0:
                    l +=1
                    while l < r and nums[l] == nums[l-1] :
                        l +=1
            
                elif sum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1] :
                        r -= 1
                else :
                    res.append([nums[k],nums[l],nums[r]])
                    l +=1
                    r-=1
                    while l < r and nums[r] == nums[r+1] :
                        r -= 1
                    while l < r and nums[l] == nums[l-1] :
                        l +=1
                
        return res



            
