class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + f"{len(s)}" + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):
            numS = ""
            # Get the first number
            while s[i] != "#":
                numS = numS + s[i]
                i +=1
                
            # convert it into int
            numI = int(numS)
            
            # loop over #
            i +=1
            word = s[i:numI+i]
            res.append(word)
            i += numI
        
        return res
  


            
            

        
