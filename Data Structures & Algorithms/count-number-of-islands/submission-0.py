class Solution:

    def dfs(self, grid, row, col):
       if grid[row][col] !=  '1': return
       grid[row][col] = '.'
       if row > 0: self.dfs(grid, row-1, col)
       if row < len(grid) - 1: self.dfs(grid, row+1, col)
       if col > 0: self.dfs(grid, row, col-1)
       if col < len(grid[0]) - 1: self.dfs(grid, row, col+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count+=1
        return count