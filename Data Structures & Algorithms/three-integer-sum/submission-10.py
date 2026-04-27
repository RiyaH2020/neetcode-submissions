class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if (i>0 and nums[i-1]==nums[i]):
                continue
            t=-nums[i]
            left=i+1
            right=len(nums)-1
            while(left<right):
                if(nums[left]+nums[right]==t):
                    res.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif(nums[left]+nums[right]<t):
                    left=left+1
                else:
                    right=right-1
        return res

        

                    
        