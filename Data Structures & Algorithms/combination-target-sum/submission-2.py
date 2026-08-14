class Solution:

    def helper(self, nums, index, target, found, curr):
        if target == 0: found.append(curr.copy())
        if target <= 0: return
        for idx in range(index, len(nums)):
            if nums[idx] > target: return
            curr.append(nums[idx])
            self.helper(nums, idx, target - nums[idx], found, curr)
            curr.pop()



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        found = []
        self.helper(sorted(nums), 0, target, found, [])
        return found