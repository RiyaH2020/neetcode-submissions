class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def is_palindrome(sub):
            return sub==sub[::-1]
        def helper(start):
            if(start==len(s)):
                res.append(path[:])
                return
            for end in range(start,len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    helper(end+1)
                    path.pop()
            return
        helper(0)
        return res

