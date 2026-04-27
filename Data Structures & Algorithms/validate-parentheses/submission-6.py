class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if(c==']' or c=='}' or c==')'):
                if(stack):
                    top=stack.pop()
                    if(c==']' and top=='['):
                        continue
                    elif(c==')' and top=='('):
                        continue
                    elif(c=='}' and top=='{'):
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        if(len(stack)==0):
            return True
        else:
            return False
        