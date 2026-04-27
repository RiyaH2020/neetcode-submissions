class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashDict={}
        l=0
        maxLen=0
        maxCount=0
        for r in range(len(s)):
            if(s[r] in hashDict):
                hashDict[s[r]]+=1
            else:
                hashDict[s[r]]=1
            maxCount=max(maxCount,hashDict[s[r]])
            while(r-l+1-maxCount>k):
                if(hashDict[s[l]]==1):
                    del hashDict[s[l]]
                else:
                    hashDict[s[l]]-=1
                l=l+1
            maxLen=max(maxLen,r-l+1)
        return maxLen