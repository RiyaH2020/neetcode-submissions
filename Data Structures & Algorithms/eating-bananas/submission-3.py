class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        minIndex=float('inf')
        while(left<=right):
            mid=(left+right)//2
            hours=0
            for i in range(len(piles)):
                if(piles[i]<mid):
                    hours=hours+1
                else:
                    hours=hours+math.ceil(piles[i]/mid)
            if(hours<=h):
                minIndex=min(mid,minIndex)
                right=mid-1
            else:
                left=mid+1
        return minIndex
        