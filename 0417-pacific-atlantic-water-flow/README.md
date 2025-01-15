# Pacific Atlantic Water Flow (Leetcode #417)

The **Pacific Atlantic Water Flow** problem (LeetCode #417) is an interesting challenge that asks us to determine which land cells in a given matrix can flow to both the Pacific and Atlantic oceans. Given a matrix where each cell contains a height value, water can flow from one cell to another only if the other cell is of equal or lower elevation, and water can flow to the edges of the matrix, representing the oceans.

## Understanding the Problem Statement

The matrix consists of rows and columns representing land elevations, and we need to determine which cells have the capability to reach both oceans. The top and left edges of the matrix are adjacent to the Pacific Ocean, while the bottom and right edges are adjacent to the Atlantic Ocean.

Water can only flow **downhill or laterally**, meaning that it can flow from one cell to another if the other cell is of **equal or lesser height**. The task is to return all the coordinates from which water can reach **both the Pacific and Atlantic oceans**.

## Brute Force Approach

A common brute force approach would involve simulating the flow of water from every cell in the matrix and attempting to determine whether it reaches both oceans. This can be done using a depth-first search (DFS) or breadth-first search (BFS) for each individual cell in the matrix to explore all possible paths. Although this approach is straightforward, it becomes very **inefficient** as the size of the matrix grows due to redundant computations.

The time complexity of such an approach is **O(m \* n \* (m + n))**, where **m** and **n** are the number of rows and columns, respectively. This is because we perform a DFS/BFS starting from each cell in the matrix, resulting in substantial overlapping work.

## Hint to Solve the Problem Efficiently

To improve upon the brute force approach, consider **reversing the problem**: instead of starting from every cell and trying to determine whether it can reach both oceans, start from the oceans and try to determine which cells can be reached. By performing a DFS from all cells adjacent to the oceans, we can track the cells that are reachable by both the Pacific and Atlantic oceans.

## Efficient Solution

The provided solution leverages **two DFS searches** to efficiently determine which cells can reach both oceans. Here is the breakdown of the approach:

1. **Initialization**: Create two matrices to keep track of whether each cell is reachable from the **Pacific** and **Atlantic** oceans. Each matrix has the same dimensions as the input matrix, initialized to `False`.
    
2. **DFS Function**: Implement a DFS function that takes in the current cell coordinates and marks all reachable cells in the direction of increasing height.
    
3. **Pacific and Atlantic DFS**: Perform a DFS from all cells adjacent to the **Pacific Ocean** (top row and left column) to mark all cells that can reach the Pacific. Similarly, perform a DFS from all cells adjacent to the **Atlantic Ocean** (bottom row and right column).
    
4. **Find Intersecting Cells**: Iterate through the matrix to identify cells that are reachable from both the **Pacific** and **Atlantic** oceans.
    

Here is the efficient solution code:

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        pacificReachable = [[False for _ in range(n)] for _ in range(m)]
        atlanticReachable = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(row, col, reachable):
            reachable[row][col] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if (0 <= newRow < m and 0 <= newCol < n and not reachable[newRow][newCol] and
                heights[newRow][newCol] >= heights[row][col]):
                    dfs(newRow, newCol, reachable)
        
        for i in range(m):
            dfs(i, 0, pacificReachable)
            dfs(i, n - 1, atlanticReachable)
        
        for j in range(n):
            dfs(0, j, pacificReachable)
            dfs(m - 1, j, atlanticReachable)
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacificReachable[i][j] and atlanticReachable[i][j]:
                    result.append([i, j])
        
        return result
```

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(m \* n)**, where **m** is the number of rows and **n** is the number of columns. This is because each cell is visited once during the DFS for both oceans, resulting in a linear pass through the entire matrix.
    
* **Space Complexity**: The space complexity is **O(m \* n)** for storing the reachability matrices and **O(m \* n)** for the recursion stack in the worst case where all cells are traversed. Therefore, the overall space complexity is **O(m \* n)**.
    

## Conclusion

The Pacific Atlantic Water Flow problem can be efficiently solved by leveraging the idea of starting from the oceans and marking reachable cells using depth-first search. This approach reduces redundant calculations and allows for a more streamlined solution compared to the brute force method. By using two separate DFS traversals from the Pacific and Atlantic oceans, we can effectively identify the cells that have the ability to reach both bodies of water. This problem is an excellent example of how reversing the perspective can lead to a significant improvement in efficiency.


README for [Pacific Atlantic Water Flow (Leetcode #417)](https://blog.unwiredlearning.com/pacific-atlantic-water-flow) was compiled from the Unwired Learning Blog.