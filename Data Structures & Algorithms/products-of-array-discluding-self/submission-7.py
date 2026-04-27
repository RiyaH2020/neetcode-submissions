class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*(len(nums))
        t=1
        for i in range(len(nums)):
            prefix[i]=t
            t=t*nums[i]
        s=1
        for i in range(len(nums)-1,-1,-1):
            prefix[i]=s*prefix[i]
            s=s*nums[i]
        return prefix
