class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def helper(i,temp):
            res.append(temp[:])
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                temp.append(nums[j])
                helper(j+1,temp)
                temp.pop()
            return
        helper(0,[])
        return res
        