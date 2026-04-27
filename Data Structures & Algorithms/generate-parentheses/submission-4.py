class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(left,right,temp):
            if(left==0 and right==0):
                res.append(temp)
                return
            if(left>0):
                dfs(left-1,right,temp+"(")
            if(right>left):
                dfs(left,right-1,temp+")")
        dfs(n,n,"")
        return res
            
            
                