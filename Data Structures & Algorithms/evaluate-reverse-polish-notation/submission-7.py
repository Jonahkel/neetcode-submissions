
def is_number(token:str) -> bool:
    try:
        int(token)
        return True
    except ValueError:
        return False

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if is_number(token): num_stack.append(int(token))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                if token == '+':
                    num_stack.append(num1+num2)
                elif token == '-':
                    num_stack.append(num1-num2)
                elif token == '*':
                    num_stack.append(num1*num2)
                elif token == '/':
                    num_stack.append(int(num1/num2))
        return num_stack[0]
