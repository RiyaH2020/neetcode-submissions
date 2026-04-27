class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,target,temp):
            if(target<0 or i>=len(nums)):
                return
            if(target==0):
                res.append(temp[:])
                return
            
            temp.append(nums[i])
            dfs(i,target-nums[i],temp)
            temp.pop()
            dfs(i+1,target,temp)

        dfs(0,target,[])
        return res

            
