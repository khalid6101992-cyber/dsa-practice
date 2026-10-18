class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_price = 0
        for index, price in enumerate(prices):

            if price < min_price:
                min_price = price
            
            max_price = max(max_price, prices[index] - min_price)

        return max_price
        