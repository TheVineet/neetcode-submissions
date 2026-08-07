class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int)
        dictT = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            dictS[s[i]] +=1
            dictT[t[i]] +=1
        
        if dictS != dictT:
            return False
        
        return True

