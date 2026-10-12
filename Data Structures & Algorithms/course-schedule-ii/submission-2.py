class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            preMap[c1].append(c2)
        done = set()
        res = []
        def dfs(course, visit, done):
            if course in visit:
                return False
            
            if course in done:
                return True
            
            visit.add(course)
            for preq in preMap[course]:
                if not dfs(preq, visit, done):
                    return False
            
            visit.remove(course)
            done.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course,set(),done):
                return []
        
        return res
