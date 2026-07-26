class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_left = [0] * len(prices)
        max_right = [0] * len(prices)
        for idx, price in enumerate(prices):
            if idx == 0:
                min_left[idx] = prices[idx]
            else:
                min_left[idx] = min(min_left[idx-1], prices[idx])
        for idx, price in enumerate(reversed(prices)):
            og_idx = len(prices) - 1 - idx
            if og_idx == len(prices) - 1:
                max_right[og_idx] = prices[og_idx]
            else:
                max_right[og_idx] = max(prices[og_idx], max_right[og_idx+1])
    
        return max(right - left for left, right in zip(min_left, max_right))                