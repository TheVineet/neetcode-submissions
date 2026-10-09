class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Map each course to prerequisite
        # Initialise empty map
        preMap = {i : [] for i in range(numCourses)}

        for pre in prerequisites:
            preMap[pre[0]].append(pre[1])
        
        def dfs(course, visit):
            if course in visit:
                return False
            
            if preMap[course] == []:
                return True
            
            visit.add(course)
            for preq in preMap[course]:
                if not dfs(preq, visit):
                    return False
            
            visit.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course,set()):
                return False
        return True
