# Set Matrix Zeroes (Leetcode #73)

In this blog post, we will solve a popular problem from LeetCode - the "Set Matrix Zeroes" problem. It's an interesting challenge that can be approached in various ways, from basic brute force to more efficient solutions. Here, we will explore the problem, discuss the naive approach, and eventually arrive at a more optimized solution.

## Understanding the Problem Statement

The problem asks you to modify a given matrix such that if an element in the matrix is zero, you need to set its entire row and column to zero. This has to be done **in place**, meaning you can't use any additional matrix. The problem can be tricky, especially when trying to achieve optimal time and space complexity.

To better understand, let's consider an example. If given the matrix:

```python
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```

The modified output should be:

```python
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```

The challenge is to mark the rows and columns with zero efficiently while keeping the algorithm's space usage minimal.

## Brute Force Approach

A simple brute-force approach involves creating an additional matrix of the same dimensions to track where the zeros should go. You iterate through the matrix, and whenever you find a zero, you mark the corresponding row and column in the additional matrix. After identifying all such positions, you modify the original matrix accordingly.

This method is straightforward, but it requires extra space proportional to the size of the matrix, which results in **O(m \* n)** space complexity. This may not be acceptable for larger matrices, as it defies the requirement of doing it **in place**.

## Hint to Solve the Problem Efficiently

The key to solving the problem efficiently lies in using the **first row and first column** of the matrix itself to store the information about which rows and columns should be zeroed. By doing so, we can eliminate the need for an extra matrix, thus reducing space complexity.

## Efficient Solution

Let's walk through the efficient solution provided in the code:

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False
        
        # if the first row or first column need to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Use first row and column to mark zero rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out marked rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        # Zero out the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
```

In this solution, we first check if the **first row** and **first column** need to be zeroed. We use two boolean flags (`first_row_zero` and `first_col_zero`) to track this.

Next, we traverse through the rest of the matrix, and whenever we find a zero, we mark the corresponding **first row** and **first column** elements as zero. This allows us to use the first row and column as a reference for zeroing the rest of the matrix.

Finally, we traverse the matrix again, zeroing out elements based on the markers in the first row and column. In the end, we handle the first row and first column separately, if needed.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(m \* n)**, where `m` is the number of rows and `n` is the number of columns. This is because we traverse the entire matrix a few times, but each traversal is linear.
    
* **Space Complexity**: The space complexity is **O(1)**, as we are not using any additional data structures, just a few boolean variables.
    

## Conclusion

The "Set Matrix Zeroes" problem is an excellent exercise for understanding in-place modification of data structures while keeping track of necessary information efficiently. By using the first row and column as markers, we are able to significantly improve space efficiency compared to the brute-force approach.

Try implementing this solution and see how it can be applied to similar matrix-related problems. Happy coding!

README for [Set Matrix Zeroes (Leetcode #73)](https://blog.unwiredlearning.com/set-matrix-zeroes) was compiled from the Unwired Learning Blog.