class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[0]*len(nums)
        backward=[0]*len(nums)
        complete=[0]*len(nums)
        forward[0]=1
        for i in range(1,len(nums)):
            forward[i]=forward[i-1]*nums[i-1]
        backward[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            backward[i]=backward[i+1]*nums[i+1]
        for i in range(len(nums)):
            complete[i]=forward[i]*backward[i]
        return complete
        


        