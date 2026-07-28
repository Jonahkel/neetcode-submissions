class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for left_idx in range(len(s2) - len(s1)+1):
            if Counter(s1) == Counter(s2[left_idx:left_idx+len(s1)]):
                return True
        return False

        