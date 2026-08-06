class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            rate = (l+r)//2
            time = sum(-(pile_size // -rate) for pile_size in piles)
            if time > h:
                l = rate+1
            else:
                r = rate
        return l