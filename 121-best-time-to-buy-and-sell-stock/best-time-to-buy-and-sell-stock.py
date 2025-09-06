class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min >  maxprofit:
                maxprofit = prices[i] - min

        return maxprofit          
