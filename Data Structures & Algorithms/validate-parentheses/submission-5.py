class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if(c=='(' or c=='{' or c=='[' ):
                stack.append(c)
            else:
                if(c==']'):
                    top=len(stack)-1
                    if(top>=0 and stack[top]=='['):
                        stack.pop()
                    else:
                        return False
                if(c=='}'):
                    top=len(stack)-1
                    if(top>=0 and stack[top]=='{'):
                        stack.pop()
                    else:
                        return False
                if(c==')'):
                    top=len(stack)-1
                    if(top>=0 and stack[top]=='('):
                        stack.pop()
                    else:
                        return False
        if(len(stack)==0):
            return True
        else:
            return False

        