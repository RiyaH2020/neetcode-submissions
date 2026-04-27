class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            t=-nums[i]
            left=i+1
            right=len(nums)-1
            while(left<right):
                if(nums[left]+nums[right]==t):
                    res.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                elif(nums[left]+nums[right]<t):
                    left=left+1
                else:
                    right=right-1
        t1=[tuple(l1) for l1 in res]
        s1=set(t1)
        list2=[list(l1) for l1 in s1]
        return list2

                    
        