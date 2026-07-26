class Solution:
    def trap(self, height: List[int]) -> int:
        l_idx = 0
        r_idx = len(height) - 1
        max_l_height = 0
        max_r_height = 0
        water_area = 0
        while l_idx < r_idx:
            l_height = height[l_idx]
            r_height = height[r_idx]
            if l_height < min(max_l_height, max_r_height):
                water_area += min(max_l_height, max_r_height) - l_height
            if r_height < min(max_l_height, max_r_height):
                water_area += min(max_l_height, max_r_height) - r_height
            max_l_height = max(max_l_height, l_height)
            max_r_height = max(max_r_height, r_height)
            if (l_height < r_height): l_idx += 1
            else: r_idx -= 1

        return water_area
