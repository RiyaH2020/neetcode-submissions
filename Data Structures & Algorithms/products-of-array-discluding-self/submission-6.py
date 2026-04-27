class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[1]*len(nums)
        backward=[1]*len(nums)
        prod=1
        for i in range(len(nums)):
            forward[i]=prod
            prod=prod*nums[i]
        prod_2=1
        for j in range(len(nums)-1,-1,-1):
            backward[j]=prod_2
            prod_2=prod_2*nums[j]
        for i in range(len(nums)):
            forward[i]=forward[i]*backward[i]
        return forward
