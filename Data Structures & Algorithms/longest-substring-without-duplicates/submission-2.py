class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_idx = 0
        right_idx = 0
        seen_map = {}
        max_length = 0
        while right_idx < len(s):
            right_char = s[right_idx]
            if right_char in seen_map:
                left_idx = max(left_idx, seen_map[right_char] + 1)
            seen_map[right_char] = right_idx
            max_length = max(max_length, right_idx - left_idx + 1)
            right_idx += 1
        return max_length