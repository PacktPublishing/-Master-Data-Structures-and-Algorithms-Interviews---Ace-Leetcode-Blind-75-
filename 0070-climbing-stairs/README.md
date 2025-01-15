# Climbing Stairs (Leetcode 70)

The "Climbing Stairs" problem is a popular challenge often encountered in coding interviews. It provides a great opportunity to learn about dynamic programming and how to optimize a naive approach into an efficient solution. In this blog, we will explore different approaches to solving the problem, including brute force and an efficient dynamic programming solution.

## Understanding the Problem Statement

The "Climbing Stairs" problem is a common question in coding interviews and on platforms like LeetCode. The task is quite simple: given a staircase with *n* steps, you can either climb 1 or 2 steps at a time. The question is: in how many distinct ways can you climb to the top? For instance, if there are 3 steps, the distinct ways to reach the top are (1, 1, 1), (1, 2), and (2, 1), totaling 3 ways.

## Brute Force Approach

A straightforward approach to solving this problem would be using recursion, where each call represents climbing either 1 or 2 steps. For every step, you can make two choices: step 1 or step 2. By breaking down the problem recursively, you essentially form a tree of possible outcomes. This approach, however, becomes very inefficient as the number of steps increases, with repeated calculations leading to exponential time complexity.

## Hint to Solve the Problem Efficiently

The key to solving this problem lies in observing that it has overlapping subproblems. The number of ways to reach step *n* is the sum of the number of ways to reach step *n-1* and step *n-2*. This observation indicates that we can apply a dynamic programming approach to solve it efficiently.

## Efficient Solution

The efficient solution involves using a dynamic programming technique, as provided in the code below:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: if n is 1, there's only one way.
        if n == 1:
            return n
        
        # Initialize a list to store the number of ways to reach each step.
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        
        # Start calculating from the 3rd step up to the nth step.
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        # dp[n] contains the total number of ways to climb n stairs.
        return dp[n]
```

This solution leverages an array `dp` where `dp[i]` represents the number of distinct ways to reach step `i`. We start by initializing `dp[1]` and `dp[2]` since the number of ways to reach the first and second steps are known directly (1 and 2 ways, respectively). From the third step onward, each step can be reached either from the previous step or by skipping a step, leading to the relation `dp[i] = dp[i - 1] + dp[i - 2]`.

## Time and Space Complexity

The time complexity of this solution is **O(n)** because we calculate the number of ways for each step from 1 to *n* exactly once. The space complexity is **O(n)** due to the use of the `dp` array to store the results for each step. While this is efficient, further optimization is possible by reducing the space complexity to **O(1)** if only the last two results are stored instead of maintaining a full array.

## Conclusion

The "Climbing Stairs" problem is a great example to demonstrate the power of dynamic programming. While a brute force approach may seem straightforward, it quickly becomes impractical for larger inputs. By leveraging dynamic programming, we can reduce both time and space complexities to create a more efficient solution. Understanding this problem helps build a strong foundation in recognizing and solving overlapping subproblems, a crucial skill for tackling more advanced coding challenges.


README for [Climbing Stairs (Leetcode 70)](https://blog.unwiredlearning.com/climbing-stairs) was compiled from the Unwired Learning Blog.