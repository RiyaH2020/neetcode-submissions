class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,temp):
            if(i>=len(nums)):
                res.append(temp[:])
                return
            temp.append(nums[i])
            dfs(i+1,temp)
            temp.pop()
            next_index=i+1
            while next_index<len(nums) and nums[next_index]==nums[i]:
                next_index+=1
            dfs(next_index,temp)
        dfs(0,[])
        return res
