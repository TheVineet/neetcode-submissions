class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adjMap = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        
        visit = set()

        def dfs(n, prev):
            if n in visit:
                return False
            
            visit.add(n)

            for adj in adjMap[n]:
                if adj == prev:
                    continue
                if not dfs(adj,n):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n
            
            

        