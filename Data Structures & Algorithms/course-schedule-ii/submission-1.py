class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a pre requisite map
        preMap = {i : [] for i in range(numCourses)}

        for course,preq in prerequisites:
            preMap[course].append(preq)
        
        res = []

        def dfs(course,visit,done):
            if course in visit:
                return False
            
            if course in done:
                return True
            
            visit.add(course)
            for preq in preMap[course]:
                if not dfs(preq,visit,done):
                    return False
            
            visit.remove(course)
            res.append(course)
            done.add(course)
            return True
        
        done = set()

        for course in range(numCourses):
            if not dfs(course, set(), done):
                return []

        return res
            