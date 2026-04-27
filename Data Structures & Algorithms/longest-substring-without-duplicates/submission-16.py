class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l = 0
        maxLen = 0
        
        for r in range(len(s)):
            if s[r] not in hashSet:
                hashSet.add(s[r])
            else:
                while s[r] in hashSet:
                    hashSet.remove(s[l])
                    l += 1
                hashSet.add(s[r])
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
