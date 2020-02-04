class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        profit = 0 
        for price in prices:
            profit = max(profit, price - min_val)
            min_val = min(min_val, price)
        return profit