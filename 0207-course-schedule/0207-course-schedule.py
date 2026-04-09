class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for cr, pr in prerequisites:
            if cr == pr:
                return False
            preMap[cr].append(pr)
        
        visited = set()

        def dfs(cr):
            
            if cr in visited:
                return False
            if preMap[cr] == []:
                return True

            visited.add(cr)
            for pr in preMap[cr]:
                if not dfs(pr):
                    return False
            
            visited.remove(cr)
            preMap[cr] = []
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
