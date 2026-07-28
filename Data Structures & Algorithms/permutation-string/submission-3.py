class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)-1])
        for left_idx in range(len(s2) - len(s1)+1):
            s2_counter[s2[left_idx+len(s1)-1]] += 1
            if s1_counter == Counter(s2[left_idx:left_idx+len(s1)]):
                return True
            s2_counter[s2[left_idx]] -= 1
        return False

        