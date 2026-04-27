class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c for c in s if c.isalnum())
        left=0
        right=len(s)-1
        while(left<=right):
            if(s[left].lower()!=s[right].lower()):
                return False
            left=left+1
            right=right-1
        return True
        
        