class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                sol[top] = idx - top
            stack.append(idx)
        
        return sol