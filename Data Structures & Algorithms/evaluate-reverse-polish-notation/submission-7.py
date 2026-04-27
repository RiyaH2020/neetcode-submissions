class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        s=tokens
        for i in range(len(s)):
            if(s[i].lstrip('-').isdigit()):
                stack.append(int(s[i]))
            else:
                ele1=stack.pop()
                ele2=stack.pop()
                if(s[i]=="*"):
                    stack.append(ele1*ele2)
                elif(s[i]=="-"):
                    stack.append(ele2-ele1)
                elif(s[i]=="+"):
                    stack.append(ele1+ele2)
                elif(s[i]=="/"):
                    stack.append(int(ele2/ele1))
        return stack[-1]