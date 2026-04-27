class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left=1
        right=max(piles)
        min_index=float('inf')
        while(left<=right):
            mid=(left+right)//2
            i=0
            hours=0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if(hours<=h):
                min_index=min(min_index,mid)
                right=mid-1
            elif(hours>h):
                left=mid+1
        return min_index




        