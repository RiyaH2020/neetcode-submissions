class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(remaining,temp):
            if not remaining:
                res.append(temp[:])
                return
            for i in range(len(remaining)):
                temp.append(remaining[i])
                dfs(remaining[:i]+remaining[i+1:],temp)
                temp.pop()
        dfs(nums,[])
        return res                
