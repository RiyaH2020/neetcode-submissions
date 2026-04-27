class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[c.lower() for c in s if c.isalnum()]
        print(s1[-1:])
        return (s1==s1[::-1])
        