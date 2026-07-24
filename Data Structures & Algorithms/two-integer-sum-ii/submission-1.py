class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front_idx = 0
        back_idx = len(numbers) - 1
        while front_idx < back_idx:
            front_num = numbers[front_idx]
            back_num = numbers[back_idx]
            curr_sum = front_num + back_num
            if curr_sum < target:
                front_idx += 1
            elif curr_sum > target:
                back_idx -= 1
            else:
                return [front_idx+1, back_idx+1]
        raise(RuntimeError("wut"))