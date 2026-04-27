class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(i,temp):
            if(i>=len(nums)):
                res.append(temp[:])
                return
            temp.append(nums[i])
            helper(i+1,temp)
            temp.pop()
            helper(i+1,temp)
            return
        helper(0,[])
        return res

