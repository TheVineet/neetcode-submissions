class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i,curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # left side include nums[i]
            curr.append(nums[i])
            dfs(i +1, curr)

            # right side skip nums[i]
            curr.pop()
            # skip over all repeated nums[i]
            while i + 1 < len(nums) and nums[i +1] == nums[i]:
                i +=1
            dfs(i + 1, curr)
        
        dfs(0,[])
        return res


        