class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        min1=float('inf')
        while(left<=right):
            mid=(left+right)//2
            min1=min(min1,nums[mid])
            if(nums[mid]>=nums[right]):
                left=mid+1
            else:
                right=mid
        return min1
        