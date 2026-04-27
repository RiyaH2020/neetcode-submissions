class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,target,temp):
            if(i>=len(nums)):
                return
            if(target==0):
                res.append(temp[:])
                return
            if(target<0):
                return
            temp.append(nums[i])
            helper(i,target-nums[i],temp)
            temp.pop()
            helper(i+1,target,temp)
            return
        helper(0,target,[])
        return res
        