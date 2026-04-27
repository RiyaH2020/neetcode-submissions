class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        maxfreq=0
        maxLen=0
        count={}
        while(right<len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxfreq=max(count[s[right]],maxfreq)
            while(right-left+1-maxfreq>k):
                count[s[left]]=count[s[left]]-1
                left=left+1
            maxLen=max(maxLen,right-left+1)
            right=right+1
        return maxLen

