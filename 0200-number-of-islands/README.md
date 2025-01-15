# Number of Islands (Leetcode #200)

In this blog, we will explore the "Number of Islands" problem, a common coding question that helps in understanding grid traversal techniques. We'll break down the problem, explore different approaches, and provide an optimized solution.

## Understanding the Problem Statement

The "Number of Islands" problem challenges developers to determine how many distinct islands are present in a given 2D grid map. Each cell in the grid can either be land ('1') or water ('0'), and an island is formed by connecting adjacent lands horizontally or vertically. This problem is frequently asked in technical interviews and tests one's understanding of graph traversal techniques and efficient handling of matrix data structures.

## Brute Force Approach

The brute force solution to the "Number of Islands" problem involves iterating over each cell in the grid. Whenever we encounter a land cell ('1'), we count it as a potential island, then proceed to mark all the connected land cells as water ('0') to ensure that the same island is not counted multiple times. This can be done using simple iteration or a naive search. However, this approach may involve repeated traversals of the same sections of the grid, which results in inefficiency.

## Hint to Solve the Problem Efficiently

An efficient way to solve the problem is to think about how to traverse each part of the grid only once and mark it effectively. Consider implementing a Depth First Search (DFS) or Breadth First Search (BFS) approach that will help to mark all connected land cells as visited. This ensures that once an island is counted, we don't recount any of its parts.

## Efficient Solution

Below is an efficient solution that follows the provided code, leveraging Depth First Search (DFS) to explore and mark islands:

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Depth First Search (DFS) function to mark visited land
        def dfs(i, j):
            # Base case: if the index is out of bounds or the cell is water ('0'), return
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or grid[i][j] == '0'):
                return
            
            grid[i][j] = '0'  # Mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0

        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count
```

In this solution, we define a nested `dfs()` function that takes the current cell coordinates (`i`, `j`). The `dfs()` function is called recursively to traverse all adjacent land cells, marking them as visited by changing their value to '0'. This ensures that we don't count the same island multiple times.

## Time and Space Complexity

* **Time Complexity:** The time complexity of this solution is **O(M \* N)**, where **M** is the number of rows and **N** is the number of columns in the grid. Each cell is visited once, and the DFS operation runs in constant time relative to the number of cells.
    
* **Space Complexity:** The space complexity is **O(M \* N)** in the worst case due to the recursion stack, especially if the entire grid is filled with land. In the average scenario, the space complexity depends on the depth of the recursion.
    

## Conclusion

The "Number of Islands" problem is a great way to practice grid traversal techniques, particularly using Depth First Search (DFS) or Breadth First Search (BFS). By implementing an efficient solution, we can minimize redundant operations and achieve optimal performance. Mastering this approach not only helps in solving similar problems involving grids but also strengthens your understanding of recursion and graph algorithms, which are key components of technical interviews.


README for [Number of Islands (Leetcode #200)](https://blog.unwiredlearning.com/number-of-islands) was compiled from the Unwired Learning Blog.