class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_mapping = {'}':'{', ')':'(', ']':'['}
        for char in s:
            if char in paren_mapping:
                if not stack or stack.pop() != paren_mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack