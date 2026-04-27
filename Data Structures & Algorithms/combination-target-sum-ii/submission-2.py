class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=candidates
        nums.sort()
        def helper(i,target,temp):
            if(target==0):
                res.append(temp[:])
                return
            if(i>=len(nums) or target<0):
                return
            for j in range(i,len(nums)):
                if(j>i and nums[j]==nums[j-1]):
                    continue
                temp.append(nums[j])
                helper(j+1,target-nums[j],temp)
                temp.pop()
            return
        helper(0,target,[])
       
        return res