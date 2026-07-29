class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        deq = deque()
        l_idx = 0
        for r_idx, num in enumerate(nums):
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(r_idx)
            if r_idx >= k-1:
                sol.append(nums[deq[0]])
                l_idx += 1
                if deq[0] < l_idx: deq.popleft()
        return sol

