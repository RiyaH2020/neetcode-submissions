class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def isPalindrome(s1):
            return s1[:]==s1[::-1]
        def dfs(i,temp):
            if(i==len(s)):
                res.append(temp[:])
                return

            for end in range(i,len(s)):
                sub=s[i:end+1]
                if isPalindrome(sub):
                    temp.append(sub)
                    dfs(end+1,temp)
                    temp.pop()
        dfs(0,[])
        return res
                
            