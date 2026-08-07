class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sorted_nums = sorted(nums)

        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     left = nums[i]
        #     right = nums[j]
        #     sum = left + right
        #     if target == sum:
        #         return [i,j]
            # elif sum > target:
            #     j = j - 1
            # else:
            #     i +=1

        arr = []
        for i in range(len(nums)):
            arr.append((nums[i],i))
        
        arr.sort()

        i = 0
        j = len(arr) - 1

        while i < j:
            left = arr[i][0]
            right = arr[j][0]
            curr_sum = left + right
            if target == curr_sum:
                return [min(arr[i][1], arr[j][1]),max(arr[i][1], arr[j][1])]
            elif curr_sum > target:
                j = j - 1
            else:
                i +=1
            




            
        