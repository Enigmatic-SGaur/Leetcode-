class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold, sold, cool = -prices[0], 0, 0
        for p in prices[1:]:
            hold, sold, cool = max(hold, cool - p), hold + p, max(cool, sold)
        return max(sold, cool)