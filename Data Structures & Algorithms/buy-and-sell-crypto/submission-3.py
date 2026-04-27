class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        maxProfit=float('-inf')
        while(right<len(prices)):
            profit=prices[right]-prices[left]
            maxProfit=max(profit, maxProfit)
            if(profit<0):
                left=left+1
            else:
                right=right+1
        return maxProfit if maxProfit >0 else 0

        