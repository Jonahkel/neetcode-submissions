class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left_idx = 0
        right_idx = 0
        max_length = 0
        highest_freq = 0
        while right_idx < len(s):
            subr_length = right_idx - left_idx + 1
            next_char = s[right_idx]
            freq[next_char] += 1
            highest_freq = max(highest_freq, freq[next_char])
            while subr_length > highest_freq + k:
                left_char = s[left_idx]
                freq[left_char] -= 1
                left_idx += 1
                # highest_freq = max(freq.values())
                subr_length -= 1
            max_length = max(max_length, subr_length)
            right_idx += 1
                
        return max_length
