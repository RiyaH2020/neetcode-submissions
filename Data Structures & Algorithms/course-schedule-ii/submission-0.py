class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        seq=[]
        for c,p in prerequisites:
            preMap[c].append(p)
        visited,cycle=set(),set()
        def dfs(c):
            if(c in cycle):
                return False
            if(c in visited):
                return True
        
            cycle.add(c)
            for p in preMap[c]:
                if dfs(p)==False:
                    return False
            cycle.remove(c)
            visited.add(c)
            seq.append(c)
            return True
        for c in range(numCourses):
            if(dfs(c)==False):
                return []
        return seq
                
             

