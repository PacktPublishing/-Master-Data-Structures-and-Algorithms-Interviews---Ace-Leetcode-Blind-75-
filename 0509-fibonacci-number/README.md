# Fibonacci Number (Leetcode 509)

The Fibonacci sequence is a classic problem often encountered in interviews and coding assessments. It starts with the numbers 0 and 1, and each subsequent number is the sum of the two preceding ones. In this blog, we will break down the problem of finding the nth Fibonacci number, explore the brute force approach, and finally present an efficient solution.

## Understanding the Problem Statement

The problem is simple: Given an integer `n`, find the nth Fibonacci number, where `F(0) = 0` and `F(1) = 1`. Each term of the sequence is defined as `F(n) = F(n-1) + F(n-2)` for `n > 1`. The challenge here is to compute the value efficiently as `n` grows larger.

## Brute Force Approach

The most straightforward approach to finding the Fibonacci number is by using recursion. In a brute force solution, you can directly define the Fibonacci function as:

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
```

This method directly follows the definition of the Fibonacci sequence but has significant drawbacks in terms of efficiency. The recursive approach repeatedly recalculates the same sub-problems, leading to an exponential time complexity, making it impractical for larger values of `n`.

## Hint to Solve the Problem Efficiently

To solve the problem more efficiently, consider how we can eliminate the need for redundant calculations. Think about using a data structure to store intermediate results and avoid repeating calculations.

## Efficient Solution

A more optimal way to solve the problem is to use Dynamic Programming. By storing the results of previous computations in an array, we can build the solution iteratively and avoid recalculating values. Below is an efficient implementation according to the provided code:

```python
class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0 or 1, return n directly
        if n <= 1:
            return n

        # Initialize a list (dp) to store computed Fibonacci numbers
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1

        # Start calculating Fibonacci numbers from 2 to n
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # Return the nth Fibonacci number
        return dp[n]
```

In this solution, an array `dp` is used to store the Fibonacci numbers as they are calculated, which eliminates the need for repeated recursive calls. The values are computed iteratively, allowing for much faster execution.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(n)`, as we need to compute each Fibonacci number from `2` to `n` only once.
    
* **Space Complexity**: The space complexity is `O(n)` due to the use of the list `dp` to store the Fibonacci numbers.
    

Although the space complexity can be further reduced to `O(1)` by keeping only the last two Fibonacci numbers in variables rather than an entire list, this approach strikes a balance between clarity and efficiency for learning purposes.

## Conclusion

The Fibonacci sequence is a fundamental problem that helps illustrate the importance of choosing the right approach for efficiency. While the brute force recursive solution is easy to understand, it quickly becomes impractical for large inputs due to its exponential time complexity. By applying dynamic programming, we can significantly improve the efficiency of the solution, reducing the time complexity to `O(n)`. This approach demonstrates how storing intermediate results can lead to much faster solutions for problems involving overlapping sub-problems, making it an essential tool in any programmer's toolkit.


README for [Fibonacci Number (Leetcode 509)](https://blog.unwiredlearning.com/fibonacci-number) was compiled from the Unwired Learning Blog.