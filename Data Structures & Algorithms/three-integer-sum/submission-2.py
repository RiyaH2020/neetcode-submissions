class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(left<right):
                if(nums[i]+nums[left]+nums[right]==0):
                    list1.append((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif(nums[i]+nums[left]+nums[right]<0):
                    left=left+1
                else:
                    right=right-1
        return list(set(list1))

        