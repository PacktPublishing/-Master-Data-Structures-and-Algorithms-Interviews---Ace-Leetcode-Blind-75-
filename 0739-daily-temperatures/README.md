# Daily Temperatures (Leetcode #739)

The "Daily Temperatures" problem is a popular challenge on LeetCode, often used to test your ability to solve problems involving arrays and stacks. In this guide, we will break down the problem, explore a basic brute force approach, and then provide an efficient solution using a stack. By the end, you'll understand both the logic and the computational considerations involved in solving this problem effectively.

## Understanding the Problem Statement

The "Daily Temperatures" problem on LeetCode (Problem 739) is an interesting challenge where you're given a list of daily temperatures, and your goal is to find out how many days you have to wait until a warmer temperature occurs for each day. If no warmer temperature is ahead, you simply return 0 for that day.

For example, given the input `[73, 74, 75, 71, 69, 72, 76, 73]`, the output should be `[1, 1, 4, 2, 1, 1, 0, 0]`. Each value in the output corresponds to the number of days you must wait to experience a warmer day.  

## Brute Force Approach

The brute force way to solve this problem is to iterate over each temperature and, for each day, look ahead in the list to find the next warmer temperature. This would involve two nested loops:

* The outer loop goes through each temperature in the list.
    
* The inner loop searches for the next higher temperature, moving one day at a time.
    

Here's a simple representation of the brute force approach:  

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result
```

While this solution works, its time complexity is **O(n^2)**, which can be very inefficient for large inputs, resulting in a lot of unnecessary comparisons.

## Hint to Solve the Problem Efficiently

The key to solving this problem more efficiently is to avoid redundant comparisons and utilize an auxiliary data structure to keep track of indices. One very helpful data structure for such problems involving "next greater element" type queries is a **stack**.

To solve the problem efficiently, think about iterating through the temperatures from right to left. By doing so, you can leverage a stack to keep track of the indices of temperatures that are waiting to find a warmer day.

**Efficient Solution Using Stack**  
The given solution uses a stack to keep track of indices where the temperature is yet to find a warmer day. Here is the efficient implementation:  

```python
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
```

In this implementation, the list is traversed from right to left. Here’s how it works:

* The **stack** keeps the indices of temperatures where we are yet to determine the next warmer day.
    
* For each temperature, we **pop** elements from the stack until we find a warmer temperature or the stack becomes empty.
    
* If the stack still has elements after the popping process, it means we found a warmer temperature in the future, and the result is updated accordingly.
    
* Finally, we push the current index onto the stack.
    

This approach is efficient because each temperature is processed at most twice—once when it is added to the stack and once when it is removed. This means that the time complexity is **O(n)**, which is significantly better than the brute force approach.

## Time and Space Complexity

* **Time Complexity**: The efficient solution has a time complexity of **O(n)**, where **n** is the number of days in the temperature list. Each element is pushed and popped from the stack at most once, ensuring a linear traversal.
    
* **Space Complexity**: The space complexity is **O(n)**, as we use an additional stack to store the indices. The worst-case scenario involves a strictly decreasing sequence of temperatures, where all indices are added to the stack.
    

## Conclusion

The "Daily Temperatures" problem is a great example of how using the right data structure can dramatically improve the efficiency of a solution. By utilizing a stack, we can avoid redundant comparisons and achieve a linear time complexity, making the solution feasible for large inputs. This problem also reinforces the concept of the "next greater element," which is a common pattern in many algorithmic challenges. By mastering this approach, you will be better prepared for similar problems in the future.


README for [Daily Temperatures (Leetcode #739)](https://blog.unwiredlearning.com/daily-temperatures) was compiled from the Unwired Learning Blog.