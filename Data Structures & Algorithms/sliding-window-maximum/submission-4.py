class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for r in range(len(nums)-k+1):
            res.append(max(nums[r:r+k]))
        return res
            
