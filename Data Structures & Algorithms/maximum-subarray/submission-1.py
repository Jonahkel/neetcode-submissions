class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for idx in range(1,len(nums)):
            nums[idx] = max(nums[idx], nums[idx] + nums[idx-1])
            res = max(res, nums[idx])
        return res