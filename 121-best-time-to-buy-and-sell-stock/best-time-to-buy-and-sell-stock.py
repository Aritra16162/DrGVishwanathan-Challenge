class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2 :
            return 0 
        minPrice = prices[0]
        maxProfit = 0

        for i in range(n):
            if prices[i]<minPrice:
                minPrice = prices[i]
            else:
                profit = prices[i] - minPrice

                if profit > maxProfit:
                    maxProfit = profit 
        return maxProfit