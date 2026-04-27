class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            max_sum=max(max_sum,sum1)
            if(sum1<0):
                sum1=0
        return max_sum

