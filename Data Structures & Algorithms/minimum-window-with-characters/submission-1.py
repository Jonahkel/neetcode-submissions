class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        t_counter = defaultdict(int)
        matches = 52
        for char in t:
            if t_counter[char] == 0: matches -= 1
            t_counter[char] += 1
        
        s_counter = defaultdict(int)
        min_left_idx, min_right_idx = 0, len(s)
        left_idx = 0
        for right_idx, right_char in enumerate(s):
            s_counter[right_char] += 1
            if s_counter[right_char] == t_counter[right_char]: matches += 1
            while matches == 52:
                if right_idx - left_idx < min_right_idx - min_left_idx:
                    min_left_idx, min_right_idx = left_idx, right_idx
                left_char = s[left_idx]
                s_counter[left_char] -= 1
                if s_counter[left_char] + 1 == t_counter[left_char]: matches -= 1
                left_idx += 1
        if min_right_idx == len(s): return ''
        else: return s[min_left_idx : min_right_idx+1]