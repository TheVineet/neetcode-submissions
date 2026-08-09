class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            length = 1
            # check if num-1 exists in the set
            if num - 1 not in numSet:
                
                while num + 1 in numSet:
                    length +=1
                    num +=1
            longest = max(longest, length)
        
        return longest
                
 
            






'''
[0,3,2,5,4,6,1,1]

'''