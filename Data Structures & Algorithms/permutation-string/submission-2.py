class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sample = {}
        window = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            sample[s1[i]] = 1 + sample.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i],0)
        l = 0

        def checkAnagram():
            for k,v in sample.items():
                if k not in window:
                    return False
                if window[k] != v:
                    return False
            return True
        
        if checkAnagram():
            return True

        for r in range(len(s1), len(s2)):
            # increase the winow
            window[s2[l]] -= 1
            l +=1
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if checkAnagram():
                return True

        return False

