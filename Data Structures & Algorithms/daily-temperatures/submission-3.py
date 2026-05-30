class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                value = stack.pop()
                res[value] = index - value
            stack.append(index)
        
        return res