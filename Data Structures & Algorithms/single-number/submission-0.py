class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        canvas = 0
        for num in nums:
            canvas ^= num
        return canvas