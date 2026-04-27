class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map1={i:[] for i in range(n)}
        visit=set()
        
        for i,e in edges:
            map1[i].append(e)
            map1[e].append(i)
        def dfs(i,prev):
            if(i in visit):
                return False
            visit.add(i)
            for e in map1[i]:
                if(e==prev):
                    continue
                if(dfs(e,i)==False):
                    return False
            return True
        return dfs(0,-1) and n==len(visit)

