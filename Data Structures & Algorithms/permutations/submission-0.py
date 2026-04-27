class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(arr,temp):
            if(len(temp)==len(nums)):
                res.append(temp[:])
                return
            for j in range(len(arr)):
                temp.append(arr[j])
                helper(arr[:j]+arr[j+1:],temp)
                temp.pop()
            return
        helper(nums,[])
        return res
            
