class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n

        l_p = total //2

        if m < n :
            smaller = nums1
            bigger = nums2
        else :
            smaller = nums2
            bigger = nums1
        
        l = 0
        r = len(smaller) - 1

        while True:
            mid_s = l + (r-l)//2
            mid_b = l_p - mid_s - 2

            left_s = smaller[mid_s] if mid_s >= 0 else float("-infinity")
            right_s = smaller[mid_s + 1] if mid_s + 1 < len(smaller) else float("infinity")

            left_b = bigger[mid_b] if mid_b >= 0 else float("-infinity")
            right_b = bigger[mid_b + 1] if mid_b + 1 < len(bigger) else float("infinity")

            # if correct partition
            if right_b >= left_s and right_s >= left_b:
                if total % 2 == 0:
                    return (max(left_s, left_b) + min(right_s,right_b)) / 2
                else:
                    return min(right_s, right_b)
            elif right_b < left_s:
                r = mid_s - 1
            else:
                l = mid_s + 1

        



        



