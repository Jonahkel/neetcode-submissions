class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count == 0:
            sol = [1] * len(nums)
            prod = math.prod(nums)
            return [int(prod/num )for num in nums]
        else:
            sol = [0] * len(nums)
            if zero_count == 1:
                zero_idx = -1
                prod = 1
                for idx, num in enumerate(nums):
                    if num == 0:
                        zero_idx = idx
                    else:
                        prod *= num
                sol[zero_idx] = prod
            return sol
            
            