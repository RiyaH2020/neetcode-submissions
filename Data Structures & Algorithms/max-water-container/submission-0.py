class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=float('-inf')
        left=0
        right=len(heights)-1
        while(left<right):
            tmpArea=(min(heights[left],heights[right]))*(right-left)
            maxArea=max(tmpArea,maxArea)
            if(heights[left]<heights[right]):
                left=left+1
            else:
                right=right-1
        return maxArea

        