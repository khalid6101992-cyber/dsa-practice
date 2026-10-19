class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        max_profit = 0
        for price in prices:
            if price < min:
                min = price
            max_profit = max(max_profit, price - min)
        return max_profit