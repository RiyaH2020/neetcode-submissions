class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*(len(temperatures))
        
        for i in range(len(temperatures)):
            if not stack or temperatures[i]<temperatures[stack[-1]]:
                stack.append(i)
            else:
                
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    result[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return result




    


        