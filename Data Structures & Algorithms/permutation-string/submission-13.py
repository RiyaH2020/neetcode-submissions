class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isvalid(s):
            return sorted(s)==sorted(s1)
       
        k=len(s1)
        for  r in range(len(s2)-k+1):
            if(isvalid(s2[r:r+k])):
                return True
        return False
            