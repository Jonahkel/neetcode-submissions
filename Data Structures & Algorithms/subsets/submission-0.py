class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        self.helper(nums, 0, [], sol)
        return sol

    def helper(self, nums, idx, curr_list, sol):
        sol.append(curr_list)
        for i in range(idx, len(nums)):
            self.helper(nums, i+1, curr_list + [nums[i]], sol)
        