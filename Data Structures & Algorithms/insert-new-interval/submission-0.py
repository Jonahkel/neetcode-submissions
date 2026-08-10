import bisect
class Solution:
    # ERROR: only the starts are sorted, not the ends!
    # Though if they're not overlapping then I think it's guaranteed that the ends are sorted as well, so nvm
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_idx = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        right_idx = bisect.bisect_right(intervals, newInterval[1], key=lambda x: x[0]) - 1
        if left_idx < len(intervals): left_num = min(intervals[left_idx][0], newInterval[0])
        else: left_num = newInterval[0]
        if right_idx >= 0: right_num = max(intervals[right_idx][1], newInterval[1])
        else: right_num = newInterval[1]

        del intervals[left_idx:right_idx+1]
        intervals.insert(left_idx, [left_num, right_num])
        return intervals


