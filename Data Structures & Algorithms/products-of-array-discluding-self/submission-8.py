class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        answer=[0]*len(nums)
        prefix[0]=1
        suffix[-1]=1
        for i in range(len(nums)-1):
            prefix[i+1]=prefix[i]*nums[i]
        for j in range(len(nums)-1,0,-1):
            suffix[j-1]=suffix[j]*nums[j]
        for k in range(len(nums)):
            answer[k]=prefix[k]*suffix[k]
        return answer

        