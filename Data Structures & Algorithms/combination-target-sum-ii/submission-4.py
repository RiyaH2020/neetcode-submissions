class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,target,temp):
            if(target==0):
                res.append(temp[:])
                return
            if(target<0 or i>=len(candidates)):
                return
            temp.append(candidates[i])
            dfs(i+1,target-candidates[i],temp)
            temp.pop()
            dfs(i+1,target,temp)
        dfs(0,target,[])
        t=[tuple(sorted(r)) for r in res]
        list2=list(set(t))
        res=[list(r) for r in list2]
        return res
            