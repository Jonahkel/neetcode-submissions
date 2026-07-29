class Solution:
    
    def char_to_idx(self, char: str):
        return ord(char) - ord('A')
    
    def minWindow(self, s: str, t: str) -> str:
        t_count = [0] * 58
        matches = 52
        for char in t:
            char_idx = self.char_to_idx(char)
            if t_count[char_idx] == 0: matches -= 1
            t_count[char_idx] += 1
        
        s_count = [0] * 58
        min_left_idx, min_right_idx = 0, len(s)
        left_idx = 0
        for right_idx, char in enumerate(s):
            char_idx = self.char_to_idx(char)
            s_count[char_idx] += 1
            if s_count[char_idx] == t_count[char_idx]: matches += 1
            while matches == 52:
                if right_idx - left_idx < min_right_idx - min_left_idx:
                    min_left_idx, min_right_idx = left_idx, right_idx
                char_idx = self.char_to_idx(s[left_idx])
                s_count[char_idx] -= 1
                if s_count[char_idx] + 1 == t_count[char_idx]: matches -= 1
                left_idx += 1
        if min_right_idx == len(s): return ''
        else: return s[min_left_idx : min_right_idx+1]