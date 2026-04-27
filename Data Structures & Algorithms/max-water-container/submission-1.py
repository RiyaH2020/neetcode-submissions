class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxArea=float('-inf')
        while(left<right):
            height=min(heights[left],heights[right])
            area=height*(right-left)
            maxArea=max(area,maxArea)
            if(heights[left]>heights[right]):
                right=right-1
            else:
                left=left+1
        return maxArea

        