class Solution:
    # O(n^2) solution...could be better
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for idx, num in enumerate(nums):
            for jdx in range(len(nums)):
                if jdx != idx:
                    result[jdx] *= num        
        return result
