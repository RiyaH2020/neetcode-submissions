class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,target,temp):
            if(target==0):
                res.append(temp[:])
                return
            if(target<0 or i>=len(candidates)):
                return
            temp.append(candidates[i])
            dfs(i+1,target-candidates[i],temp)
            temp.pop()
            next_index=i+1
            while next_index<len(candidates) and candidates[next_index]==candidates[i]:
                next_index+=1
            dfs(next_index,target,temp)
        dfs(0,target,[])
       
        return res
            