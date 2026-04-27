class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[c for c in s if c.isalnum()]
        left=0
        right=len(s)-1
        s=''.join(s)
        s=s.lower()
        print(s)
        while(left<=right):
            if(s[left]!=s[right]):
                return False
            left=left+1
            right=right-1
        return True

        