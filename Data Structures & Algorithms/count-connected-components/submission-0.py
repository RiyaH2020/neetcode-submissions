class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map1={i:[] for i in range(n)}
        visit=set()
        for n,e in edges:
            map1[n].append(e)
            map1[e].append(n)
        def dfs(i):
            if(i in visit):
                return 
            visit.add(i)
            for e in map1[i]:
                dfs(e)

                    
        count=0
        for n in map1:
            if n not in visit:
                dfs(n)
                count+=1
        return count
        

                
