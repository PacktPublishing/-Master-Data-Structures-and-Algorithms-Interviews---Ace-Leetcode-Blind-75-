# Rotate Image (Leetcode #48)

When tackling coding problems, efficient solutions save time and resources. In this blog, we’ll explore how to solve Leetcode problem 48, 'Rotate Image.' We'll start by understanding the problem, cover a common brute force approach, then move to a more efficient solution to give you an edge. Whether you're preparing for technical interviews or simply sharpening your coding skills, this guide will provide a thorough breakdown, ensuring you master the logic behind matrix rotation.

## Understanding the Problem Statement

The problem 'Rotate Image' asks you to rotate a given n × n 2D matrix by 90 degrees (clockwise) **in place**. This means modifying the original matrix without using additional memory. The matrix is a square array of integers where you need to transform each element such that the entire matrix is rotated by 90 degrees clockwise.

For example:

**Input:**

```python
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```

**Output:**

```python
[
 [7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]
]
```

The problem requires you to implement the solution in place, meaning you should not use extra space for another matrix to perform the transformation.

## Brute Force Approach

A straightforward approach to solving this problem involves creating a new matrix of the same size to store the rotated values. You can iterate through each element in the original matrix and place it in the corresponding position in the new matrix.

For instance, given an element at row `i` and column `j`, you would place it in the new matrix at position `j` and column `n - i - 1`. This approach works, but it requires O(n^2) extra space, which contradicts the problem's requirements of an **in-place** solution.

**Pseudocode for Brute Force:**

```python
create new_matrix of size n x n
for i from 0 to n-1:
    for j from 0 to n-1:
        new_matrix[j][n - i - 1] = matrix[i][j]
copy new_matrix back to matrix
```

While this brute force method is easy to understand, it does not meet the problem's space complexity requirements.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, we need to avoid the use of an extra matrix. Instead, think about rotating the elements in layers, like peeling an onion. Imagine the matrix divided into several concentric layers—rotate each layer one at a time by swapping elements in groups of four.

## Efficient Solution

The efficient solution, as provided in the attached code, involves rotating the matrix **in place** by processing each layer of the matrix, starting from the outermost layer and moving inwards. Here's a detailed breakdown:

1. The matrix is divided into layers, and each layer is rotated separately.
    
2. For each layer, the elements in groups of four are swapped clockwise.
    
3. We iterate through the elements in each layer, saving one element as a temporary value and then proceeding to rotate the other three to their respective positions, finally placing the temporary value in its correct spot.
    

**Python Code:**

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Iterate over each layer of the matrix
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                # Save the temp element
                temp = matrix[i][j]

                # Move bottom-left element to top-left
                matrix[i][j] = matrix[n - j - 1][i]

                # Move bottom-right element to bottom-left
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

                # Move top-right element to bottom-right
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

                # Assign temp element to top-right
                matrix[j][n - i - 1] = temp
```

**Step-by-Step Explanation**

* **Layers**: The matrix is divided into layers, each represented by `i`, which ranges from `0` to `n // 2 - 1`.
    
* **Elements in Each Layer**: We iterate over each element in the layer using `j`, which ranges from `i` to `n - i - 1`.
    
* **Swapping Elements**: For each element, we perform a four-way swap:
    
    1. Save the top element (`temp`).
        
    2. Move the element from the left side to the top.
        
    3. Move the element from the bottom to the left.
        
    4. Move the element from the right to the bottom.
        
    5. Finally, move the saved element (`temp`) to the right.
        

This solution effectively rotates the matrix in place without using extra space.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n^2)**. This is because we iterate over each element of the matrix once, and each element is moved exactly once.
    
* **Space Complexity**: The space complexity is **O(1)**, as we do not use any extra data structures that grow with the input size. The rotation is done entirely within the input matrix.
    

## Conclusion

The 'Rotate Image' problem is a classic question that tests your understanding of in-place algorithms and matrix manipulation. While the brute force approach is easy to conceptualize, it does not meet the space requirements of the problem. The efficient solution provided here optimally rotates the matrix layer by layer, ensuring no extra space is used. Mastering this problem gives you a great foundation for dealing with more advanced in-place transformation problems in technical interviews.

Keep practicing problems like these to solidify your understanding of in-place operations and matrix transformations. Happy coding!

README for [Rotate Image (Leetcode #48)](https://blog.unwiredlearning.com/rotate-image) was compiled from the Unwired Learning Blog.