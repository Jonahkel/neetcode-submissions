class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_step = [0] * (n+1)
        ways_to_step[0], ways_to_step[1] = 1, 1
        for idx in range(2, n+1):
            ways_to_step[idx] = ways_to_step[idx-2]+ways_to_step[idx-1]
        return ways_to_step[n]
        