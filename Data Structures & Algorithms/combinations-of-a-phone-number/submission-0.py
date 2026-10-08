class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        if not digits:
            return []

        def dfs(i,curr):
            if i >= len(digits):
                res.append("".join(curr))
                return
            
            maps = lookup[digits[i]]

            for m in maps:
                curr.append(m)
                dfs(i + 1,curr)
                curr.pop()
        
        dfs(0,[])
        return res


        