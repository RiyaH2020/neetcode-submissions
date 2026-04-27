class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        product=[1]*len(nums)
        for i in range(len(nums)):
            product[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            product[i]*=suffix
            suffix*=nums[i]
        return product

        