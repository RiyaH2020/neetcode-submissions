class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            list1=[]
            for i in range(len(nums)-2):
                left=i+1
                right=len(nums)-1
                if(i>0 and nums[i]==nums[i-1]):
                    continue
                while(left<right):
                    if(nums[i]+nums[left]+nums[right]==0):
                        list1.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right=right-1
                        while (left<right and nums[left]==nums[left-1]):
                            left+=1
                        while (left<right and nums[right]==nums[right+1]):
                            right=right-1
                    elif(nums[i]+nums[left]+nums[right]<0):
                        left=left+1
                    else:
                        right=right-1
            return list1

            