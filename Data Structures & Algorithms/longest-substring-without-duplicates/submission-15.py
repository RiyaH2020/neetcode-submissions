class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        char_set=set()
        maxLen=0
        for right in range(len(s)):
            while(s[right] in char_set):
                char_set.remove(s[left])
                left=left+1
            char_set.add(s[right])
            maxLen=max(maxLen,len(char_set))
        return maxLen
            
        