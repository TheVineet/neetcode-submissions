import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r"[A-Za-z0-9]"
        l = 0
        r = len(s) - 1

        while l < r:
            while not re.fullmatch(pattern,s[l]) and l < r:
                l += 1
            while not re.fullmatch(pattern,s[r]) and l < r:
                r -= 1
            if not s[l].lower() == s[r].lower():
                return False
            else:
                l +=1
                r -= 1
        
        return True
            
            
        