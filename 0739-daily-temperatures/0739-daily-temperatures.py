class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Popping all indices with a lower or equal temperature than the current index
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # If the stack still has elements, then the next warmer temperature exists!
            if stack:
                result[i] = stack[-1] - i

            # Inserting current index in the stack
            stack.append(i)

        return result
    

#Question: https://leetcode.com/problems/daily-temperatures
#Blog: https://blog.unwiredlearning.com/daily-temperatures