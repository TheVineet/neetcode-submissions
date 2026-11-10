class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lookup = []
        for i in nums:
            if i in lookup:
                return True
            else:
                lookup.append(i)
        
        return False

    

    # space complexity = O(n)
    # Time complexity = n * 1 * 

# list append :  O(1), list.insert(index, value) = O(n)
# search in list : O(n) 

# search in O(1) : hashset, hashmap

        
        