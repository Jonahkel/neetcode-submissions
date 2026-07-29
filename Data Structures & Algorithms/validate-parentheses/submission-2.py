class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        begin_parens = {'(', '{', '['}
        for char in s:
            if char in begin_parens: stack.append(char)
            else:
                if not stack: return False
                match char:
                    case ')':
                        if stack.pop() != '(':
                            return False
                    case '}':
                        if stack.pop() != '{':
                            return False
                    case ']':
                        if stack.pop() != '[':
                            return False
        return not stack