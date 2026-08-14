class Solution:

    def helper(self, nums, idx, target, found, curr):
        if target == 0: found.append(curr.copy())
        if target <= 0: return
        if idx >= len(nums): return
        if nums[idx] > target: return
        curr.append(nums[idx])
        target -= nums[idx]
        self.helper(nums, idx, target, found, curr)
        target += nums[idx]
        curr.pop()
        idx += 1
        self.helper(nums, idx, target, found, curr)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        found = []
        self.helper(sorted(nums), 0, target, found, [])
        return found