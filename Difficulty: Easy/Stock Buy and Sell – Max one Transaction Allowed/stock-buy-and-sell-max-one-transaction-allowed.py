class Solution:
    def maximumProfit(self, prices):
        max_profit=float('-inf')
        min_price=float('inf')
        for price in prices:
            #min price so far
            min_price=min(price,min_price)
            #max profit = selling day price - min_price it was bought
            max_profit=max(max_profit,price-min_price)
        return max_profit
            