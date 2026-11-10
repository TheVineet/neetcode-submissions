class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lookup = {}
        for i in nums:
            if i in lookup:
                return True
            else:
                lookup[i] = True
        
        return False

#    {
#     1 : True,
#     2 : True,

#    }

    # space complexity = O(n)
    # Time complexity = n * 1 * n = n2

# list append :  O(1), list.insert(index, value) = O(n)
# search in list : O(n) 

# search in O(1) : hashset, hashmap

        
        