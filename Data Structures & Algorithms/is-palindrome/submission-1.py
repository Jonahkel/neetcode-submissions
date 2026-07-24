class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < len(s) and not s[front].isalnum(): front += 1
        while back >= 0 and not s[back].isalnum(): back -= 1
        while front < back:
            if s[front].lower() != s[back].lower(): return False
            front += 1
            back -= 1
            while front < len(s) and not s[front].isalnum(): front += 1
            while back >= 0 and not s[back].isalnum(): back -= 1
        return True