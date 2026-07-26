class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        max_prof = 0
        for price in prices:
            max_prof = max(max_prof, price - min_left)
            min_left = min(min_left, price)

        return max_prof                