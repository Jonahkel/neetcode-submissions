class Solution:
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr_area = 0

        def dfs(row, col):
            nonlocal curr_area
            if row not in range(len(grid)) or col not in range(len(grid[0])): return
            if grid[row][col] != 1: return
            grid[row][col] = 0
            curr_area += 1
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            return
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    curr_area = 0
                    dfs(row, col)
                    max_area = max(max_area, curr_area)
        
        return max_area
        
