class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closedN,curr):
            if openN == closedN == n:
                res.append("".join(curr))
                return
            
            if openN < n:
                # Insert open bracket
                curr.append("(")
                dfs(openN + 1, closedN, curr)
                curr.pop()
            
            if closedN < openN:
                curr.append(")")
                dfs(openN, closedN + 1, curr)
                curr.pop()
        
        dfs(0,0,[])
        return res

        