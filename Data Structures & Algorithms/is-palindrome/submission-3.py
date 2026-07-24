class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < back:
            while front < len(s)-1 and not s[front].isalnum(): front += 1
            while back >= 0 and not s[back].isalnum(): back -= 1
            if s[front].lower() != s[back].lower(): return False
            front += 1
            back -= 1
        return True