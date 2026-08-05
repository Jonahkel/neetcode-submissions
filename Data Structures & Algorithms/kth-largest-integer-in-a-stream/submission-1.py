class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:k]
        heapq.heapify(self.nums)
        self.limit = k
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.nums) < self.limit:
            heapq.heappush(self.nums, val)
            return self.nums[0]
        if val <= self.nums[0]: return self.nums[0]
        heapq.heappush(self.nums, val)
        heapq.heappop(self.nums)
        return self.nums[0]
        
