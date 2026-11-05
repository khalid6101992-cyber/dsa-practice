class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        print(temperatures)
        wait = [0] * len(temperatures)
        print(wait)
        stack = []
        for i, temp in enumerate(temperatures):
            print(temp)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                print(waiting_day)
                wait[waiting_day] = i - waiting_day
            stack.append(i)
        return wait
        