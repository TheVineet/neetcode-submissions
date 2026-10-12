class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            preMap[c1].append(c2)
        

        def dfs(i,path):
            if i in path:
                return False
            
            if  preMap[i] == []:
                return True
            
            path.add(i)
            for preq in preMap[i]:
                if not dfs(preq,path):
                    return False   

            path.remove(i)
            preMap[i] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True