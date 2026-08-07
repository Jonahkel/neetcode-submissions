from functools import cache
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(m,n):
            if m == 1 or n == 1: return 1
            return helper(m-1,n) + helper(m,n-1)
        
        return helper(m,n)