import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        # Max-heap: (-value, index)
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        res = [-heap[0][0]]  # first window max
        
        for i in range(k, len(nums)):
            # Push the new element
            heapq.heappush(heap, (-nums[i], i))
            
            # Pop elements whose index is out of the window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
        
        return res
