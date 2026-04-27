class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            n=nums[i]
            if(target-n in dict1):
                return[dict1[target-n],i]
            else:
                dict1[n]=i



        