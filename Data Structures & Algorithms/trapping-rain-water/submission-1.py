class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        total_water=0
        left_max,right_max=0,0
        while(left<=right):
            if(height[left]<height[right]):
                if(height[left]>=left_max):
                    left_max=height[left]
                else:
                    total_water+=left_max-height[left]
                left=left+1
            else:
                if(height[right]>=right_max):
                    right_max=height[right]
                else:
                    total_water+=right_max-height[right]
                right=right-1
        return total_water



        