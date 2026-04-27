class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=sum(piles)
        min_k=float('inf')
        while(left<=right):
            mid=(left+right)//2
            hours=0
            for p in piles:
                if(p<mid):
                    hours=hours+1
                else:
                    hours=hours+math.ceil(p/mid)
            if(hours<=h):
                min_k=min(min_k,mid)
                right=mid-1
            elif(hours>h):
                left=mid+1
        return min_k
            