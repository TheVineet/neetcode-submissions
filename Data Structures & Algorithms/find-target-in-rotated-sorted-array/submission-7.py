class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l)//2

            if target == nums[m]:
                return m

            # if we are in left list
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1 #got to look at the right side of mid
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 #got to look at the left side
                else:
                    l = m + 1

        return -1


        