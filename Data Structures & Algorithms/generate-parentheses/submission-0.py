class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(current,left,right):
            if(left==0 and right==0):
                res.append(current)
                return
            if(left>0):
                backtrack(current+'(',left-1,right)
            if(right>left):
                backtrack(current+')',left,right-1)
        backtrack("",n,n)
        return res

        
        
        

        