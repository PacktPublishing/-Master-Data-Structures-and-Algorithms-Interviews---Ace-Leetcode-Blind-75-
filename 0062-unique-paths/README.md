# Unique Paths (Leetcode #62)

Navigating through the Leetcode problem “Unique Paths” can be an intriguing challenge for aspiring programmers. Whether you are a beginner or a seasoned coder, understanding the efficient ways to solve this problem not only sharpens your dynamic programming skills but also enhances your ability to create optimal solutions for related challenges. In this blog, we will delve into a detailed explanation of the problem, explore a brute force approach, and then solve it efficiently with the help of a dynamic programming solution.

## Understanding the Problem Statement

The Leetcode problem 62. Unique Paths is about finding how many distinct paths exist from the top-left corner to the bottom-right corner of an `m x n` grid. The movement is restricted to either right or down at any point in time. This implies that, starting from `(0, 0)`, you must find a way to reach `(m-1, n-1)` while only moving in the allowed directions.

To put it simply, given the constraints of the grid, your job is to find how many different ways you can travel across the grid using just right and down movements.

## Brute Force Approach

A common brute force approach would involve exploring all possible paths from the starting point to the destination. This can be implemented using recursion where, at each cell, you make recursive calls to move either to the right or down. The final result will be the sum of all possible ways to reach the destination.

The recursive approach can be represented as follows:

1. Start from the cell `(0, 0)`.
    
2. For each cell, move either to the right or down until you reach the bottom-right corner.
    
3. Count each successful attempt that reaches the destination.
    

However, this approach becomes highly inefficient as the grid size increases. The overlapping subproblems lead to exponential complexity, making the solution impractical for large values of `m` and `n`.

## Hint to Solve the Problem Efficiently

To solve this problem more efficiently, you can use dynamic programming (DP) to avoid redundant calculations. The main idea is to break down the problem into smaller subproblems and store their results, so you don’t have to compute them repeatedly. Consider filling a matrix where each cell represents the number of ways to reach that cell from the top-left.

## Efficient Solution

The provided solution efficiently solves the problem using a dynamic programming (DP) table to keep track of the number of unique paths to each cell.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1 and 2: Initialize DP array with 1s
        dp = [[1]*n for _ in range(m)]  
    
        # Step 2: Fill in the dp with unique paths to each cell
        for i in range(1, m):          
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Step 3: Return the result from the bottom-right cell
        return dp[m-1][n-1]
```

**Explanation of the Code:**

1. **Initialization:** The `dp` table is initialized with 1s. This is because there is only one way to reach any cell in the first row or first column—by moving exclusively right or down, respectively.
    
2. **Filling the DP Table:** For every other cell, the number of ways to reach that cell is the sum of the number of ways to reach the cell directly above (`dp[i-1][j]`) and the number of ways to reach the cell to the left (`dp[i][j-1]`). This builds on smaller subproblems to compute the solution for the entire grid.
    
3. **Final Output:** The final answer is stored in the bottom-right cell (`dp[m-1][n-1]`), which contains the number of unique paths to reach that point.
    

## Time and Space Complexity

* **Time Complexity:** The time complexity of this solution is `O(m * n)`, as we iterate through all cells of the `m x n` grid once.
    
* **Space Complexity:** The space complexity is `O(m * n)` due to the storage requirement for the `dp` matrix. However, this can be optimized to `O(n)` by using a 1D array since we only need the current and previous row values at each step.
    

## Conclusion

The Unique Paths problem is an excellent exercise for learning dynamic programming, as it allows you to transform a recursive approach into an efficient DP solution. By utilizing a DP table, we avoid redundant calculations and solve the problem optimally. Remember, whenever you encounter overlapping subproblems, dynamic programming is a great tool to simplify the solution and achieve optimal performance.

Dynamic programming might feel challenging at first, but with practice, it will become one of the most powerful tools in your coding toolkit!

README for [Unique Paths (Leetcode #62)](https://blog.unwiredlearning.com/unique-paths) was compiled from the Unwired Learning Blog.