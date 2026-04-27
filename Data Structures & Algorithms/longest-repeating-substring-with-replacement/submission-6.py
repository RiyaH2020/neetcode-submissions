class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        seen={}
        maxLen=0
        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1
            while(right-left+1-max(seen.values())>k):
                if(s[left]==1):
                    seen.pop(s[left])
                else:
                    seen[s[left]]-=1
                left=left+1
            maxLen=max(maxLen,right-left+1)
        return maxLen