class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = max(heights)+1
        cur_areas = [0] * m
        largest = 0
        for num in heights:
            for i in range(m):
                if i <= num:
                    cur_areas[i] += i
                    largest = max(largest, cur_areas[i])
                else:
                    cur_areas[i] = 0
        return largest