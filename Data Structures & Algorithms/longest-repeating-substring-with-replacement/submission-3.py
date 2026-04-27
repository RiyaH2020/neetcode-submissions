class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        char_list={}
        maxLen=0
        while(right<len(s)):
            if(s[right] in char_list):
                char_list[s[right]]+=1
            else:
                char_list[s[right]]=1
            right=right+1
            max_count=max(char_list.values())
            if((right-left)-max_count>k):
                if(char_list[s[left]]==1):
                    char_list.pop(s[left])
                else:
                    char_list[s[left]]-=1
                left=left+1
            maxLen=max(maxLen,right-left)
        return maxLen



        