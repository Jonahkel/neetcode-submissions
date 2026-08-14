class Solution:
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(row, col):
            if row not in range(len(grid)) or col not in range(len(grid[0])): return 0
            if grid[row][col] != 1: return 0
            grid[row][col] = 0
            curr_area = 1
            curr_area += dfs(row-1, col)
            curr_area += dfs(row+1, col)
            curr_area += dfs(row, col-1)
            curr_area += dfs(row, col+1)
            return curr_area
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, dfs(row,col))
        
        return max_area
        
