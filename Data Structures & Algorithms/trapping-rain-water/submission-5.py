class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=0
        right_max=0
        area=0
        while(left<right):
            if(height[left]<=height[right]):
                if(left_max<height[left]):
                    left_max=height[left]
                else:
                    area+=left_max-height[left]
                left=left+1
            else:
                if(right_max<height[right]):
                    right_max=height[right]
                else:
                    area+=right_max-height[right]
                right=right-1
        return area