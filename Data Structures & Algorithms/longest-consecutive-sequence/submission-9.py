class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        maxLen=1
        for n in nums:
            count=1
            i=n
            while(i+1 in set1):
                count=count+1
                i=i+1
            maxLen=max(count,maxLen)
        return maxLen if nums else 0

