class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=candidates
        def helper(i,target,temp):
            if(target==0):
                res.append(temp[:])
                return
            if(i>=len(nums) or target<0):
                return
            temp.append(nums[i])
            helper(i+1,target-nums[i],temp)
            temp.pop()
            helper(i+1,target,temp)
            return
        helper(0,target,[])
        res=[sorted(r) for r in res]
        res=[tuple(r) for r in res]
        res=list(set(res))
        res=[list(r) for r in res]
        return res