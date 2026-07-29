class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        heap = [(-num, idx) for idx, num in enumerate(nums[:k-1])]
        heapq.heapify(heap)
        for l_idx in range(len(nums) - k+1):
            r_idx = l_idx + k - 1
            heapq.heappush(heap, (-nums[r_idx], r_idx))
            top_num, idx = heap[0]
            while idx < l_idx:
                heapq.heappop(heap)
                top_num, idx = heap[0]
            maxes.append(-top_num)
        return maxes