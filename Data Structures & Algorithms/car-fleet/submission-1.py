class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed), reverse=True)
        times=[(target-pos)/spd for pos,spd in cars]
        stack=[]
        for t in times:
            if not stack or t>stack[-1]:
                stack.append(t)
        return len(stack)

        
        