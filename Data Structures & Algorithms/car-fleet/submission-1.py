class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_time = -1
        fleets = 0
        rev_order = sorted(zip(position, speed), reverse=True)
        for pos,sp in rev_order:
            time = (target - pos)/sp
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets

