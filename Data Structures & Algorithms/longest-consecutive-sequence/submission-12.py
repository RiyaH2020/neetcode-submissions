class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        len1=0
        maxLen=0
        for n in nums:
            while(n in set1):
                len1+=1
                n=n+1
            maxLen=max(len1,maxLen)
            len1=0
        return maxLen
            

