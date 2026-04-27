class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(start,temp):
            if(len(temp)==len(nums)):
                res.append(temp[:])
                return
            for j in range(start,len(nums)):
                temp.append(nums[j])
                nums[start],nums[j]=nums[j],nums[start]
                helper(start+1,temp)
                temp.pop()
                nums[start],nums[j]=nums[j],nums[start]
            return
        helper(0,[])
        return res
            
