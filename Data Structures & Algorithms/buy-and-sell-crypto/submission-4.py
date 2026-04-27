class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        profit=float('-inf')
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-minPrice)
            minPrice=min(minPrice, prices[i])
        return profit if profit >0 else 0

            


        