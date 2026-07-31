class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_limit = [-1]*len(heights)
        right_limit = [len(heights)]*len(heights)
        stack = []
        for idx, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                right_limit[stack.pop()] = idx
            stack.append(idx)
        stack = []
        for idx, num in enumerate(reversed(heights)):
            idx = len(heights)-1 - idx
            while stack and heights[stack[-1]] > num:
                left_limit[stack.pop()] = idx
            stack.append(idx)
        
        return max((right_limit-left_limit-1)*height for right_limit, left_limit, height in zip(right_limit, left_limit, heights))
