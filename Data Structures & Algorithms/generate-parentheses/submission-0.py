class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closedN, curr):
            if openN == closedN == n:
                return res.append("".join(curr))
            
            if openN < n:
                curr.append("(")
                dfs(openN + 1, closedN, curr)
                curr.pop()
            
            if closedN < openN:
                curr.append(")")
                dfs(openN, closedN + 1, curr)
                curr.pop()
        
        dfs(0,0,[])

        return res
        