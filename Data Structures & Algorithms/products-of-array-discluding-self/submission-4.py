class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1=[1]*(len(nums))
        cumulative_prod=1
        for i in range(len(nums1)):
            nums1[i]=cumulative_prod
            cumulative_prod*=nums[i]
        cumulative_prod=1
        for i in range(len(nums1)-1,-1,-1):
            nums1[i]*=cumulative_prod
            cumulative_prod*=nums[i]

        return nums1

        