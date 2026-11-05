class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        wait = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                wait[waiting_day] = i - waiting_day
            stack.append(i)
        return wait
        