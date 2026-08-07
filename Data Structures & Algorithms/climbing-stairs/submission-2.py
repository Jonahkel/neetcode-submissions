def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

class Solution:

    @memoize
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        