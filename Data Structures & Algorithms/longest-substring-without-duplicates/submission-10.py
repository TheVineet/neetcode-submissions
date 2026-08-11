class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = {}
        longest = 0

        for r in range(len(s)):
            if s[r] in count:
                l = max(l, count[s[r]] + 1)
            longest = max(r-l+1,longest)
            count[s[r]] = r
        return longest




