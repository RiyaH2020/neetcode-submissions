class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        maxLen=0
        set1=set()
        while(right<len(s)):
            if(s[right] not in set1):
                set1.add(s[right])
                maxLen=max(maxLen,right-left+1)
                right=right+1
            else:
                set1.remove(s[left])
                left=left+1
        return maxLen
            

        
        