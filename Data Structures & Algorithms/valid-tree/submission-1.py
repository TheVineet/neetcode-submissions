class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        visit = set()
        def dfs(node, visit, prev):
            if node in visit:
                return False

            visit.add(node)
            for adj in adjMap[node]:
                if adj == prev:
                    continue

                if not dfs(adj,visit,node):
                    return False
            
            return True
        
        return dfs(0,visit,-1) and len(visit) == n
