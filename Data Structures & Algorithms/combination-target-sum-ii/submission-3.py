class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,total,curr):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i], curr)

            curr.pop()

            while (i + 1) < len(candidates) and candidates[i + 1] == candidates[i]:
                i +=1
            
            dfs(i + 1, total, curr)
        
        dfs(0,0,[])
        return res