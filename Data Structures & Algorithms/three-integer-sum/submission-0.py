class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while(left<right):
                if(nums[i]+nums[left]+nums[right]==0):
                    tmp_list=[nums[i],nums[left],nums[right]]
                    res.append(tmp_list)
                    left=left+1
                    right=right-1
                elif(nums[i]+nums[left]+nums[right]<0):
                    left=left+1
                else:
                    right=right-1
        return list(set(tuple(triplet) for triplet in res))

    
        