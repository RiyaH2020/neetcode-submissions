class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-w for w in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            max1=-heapq.heappop(stones)
            max2=-heapq.heappop(stones)
            if(max1!=max2):
                heapq.heappush(stones,-(max1-max2))
        


        return -stones[0] if len(stones)==1 else 0
        