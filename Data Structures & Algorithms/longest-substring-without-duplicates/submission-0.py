class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_idx = 0
        right_idx = 0
        seen_set = set()
        max_length = 0
        while right_idx < len(s):
            right_char = s[right_idx]
            if right_char in seen_set:
                while left_idx < right_idx:
                    left_char = s[left_idx]
                    seen_set.remove(left_char)
                    left_idx += 1
                    if left_char == right_char: break
            seen_set.add(right_char)
            max_length = max(max_length, right_idx - left_idx + 1)
            right_idx += 1
        return max_length