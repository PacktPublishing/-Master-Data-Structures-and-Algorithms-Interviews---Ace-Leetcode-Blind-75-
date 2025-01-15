# Word Search (Leetcode #79)

The "Word Search" problem is a challenging LeetCode problem where you are given a grid (board) filled with characters and a target word. The objective is to determine if the target word can be constructed by sequentially moving through adjacent cells in the grid. The cells can be connected either horizontally or vertically, and each letter can only be used once in a particular path.

## Understanding the Problem Statement

In the "Word Search" problem, you are given a 2D board of characters and a target word. The goal is to determine if the word can be found in the board by sequentially adjacent cells. You can move horizontally or vertically between adjacent cells, but you cannot use the same cell more than once in constructing the word. For example, given a board:

```python
[['A', 'B', 'C', 'E'],
 ['S', 'F', 'C', 'S'],
 ['A', 'D', 'E', 'E']]
```

and a word "ABCCED", the result is `True` since the word can be traced through the board starting at the top-left.

This problem can be challenging because you must explore all possible paths from each starting point and backtrack when necessary, ensuring each letter is used exactly once in each potential word match.

The "Word Search" problem is a popular LeetCode challenge that asks you to determine if a given word can be constructed by sequentially adjacent cells on a grid of letters. Adjacent cells are defined as being either horizontally or vertically neighboring. Each letter must be used only once, which means we cannot revisit a cell. This problem often tests one's ability to effectively traverse a matrix in a recursive manner, making it an excellent candidate to apply Depth-First Search (DFS).

## Brute Force Approach

The brute force approach to solve this problem is to check every cell of the board, treating each cell as a possible starting point for the word. From each cell, we recursively search in all possible directions (up, down, left, and right) until we either find the word or exhaust all possibilities. Although this approach can technically work, it is quite inefficient, especially when the grid size is large or the word length is significant. Each incorrect path has to be retraced, which makes it time-consuming.

## Hint to Solve the Problem Efficiently

A more efficient solution requires using the Depth-First Search (DFS) technique. The key observation here is that we can perform a recursive DFS search, starting from each cell, while keeping track of the word character we are currently trying to match. During the search, we must ensure that we do not revisit any character that we have already used, and also avoid exploring cells that go beyond the bounds of the board.

## Efficient Solution

The efficient solution, as seen in the provided code, uses DFS to search for the target word starting from any cell that matches the first character of the word. Here is a step-by-step breakdown of the provided code:

* **Class and Function Definition**: The solution is implemented in a class named `Solution`, with the main function `exist()` which takes in a `board` and the `word` to search for.
    
* **DFS Function**: A nested function `dfs(i, j, k)` is defined to perform the DFS operation. The parameters `i` and `j` are the current row and column indices, and `k` is the index of the current character in the word that we are trying to match.
    
* **Base Condition**: The DFS function returns `True` if `k` matches the length of the word, indicating that the entire word has been successfully matched.
    
* **Boundary and Character Check**: The function checks if the current cell `(i, j)` is out of bounds or if the current character does not match the corresponding character in the word. If either condition is true, it returns `False`.
    
* **Recursive Calls**: If the character matches, the current cell is temporarily marked as visited by setting it to a non-letter character (e.g., `/`) to avoid revisiting. Then, the DFS function is recursively called for all adjacent cells (up, down, left, and right).
    
* **Backtracking**: After all possible moves from a given cell have been tried, the cell value is restored, allowing it to be used in other recursive paths.
    
* **Iterate Over Board**: Finally, the function iterates over each cell of the board, initiating the DFS search if the character matches the first character of the word.
    

The solution effectively uses backtracking to manage the state of each cell, ensuring that we do not use the same cell twice for matching the word, while also restoring the board to its original state after exploring each path.

## Time and Space Complexity

* **Time Complexity**: The time complexity of the solution is `O(N * 3^L)`, where `N` is the total number of cells in the board and `L` is the length of the word. This is because each cell can potentially lead to three other recursive calls (excluding the direction it came from).
    
* **Space Complexity**: The space complexity is `O(L)` where `L` is the length of the word. This space is used for the recursion stack in the worst-case scenario, which occurs when the entire word is explored.
    

The use of backtracking ensures that the board is always restored to its original state after exploring each possibility, which is key to efficiently solving the problem without using additional memory for storing the state of the board.

## Conclusion

The "Word Search" problem is a great exercise in understanding how to effectively navigate a grid using recursion and backtracking. By carefully managing the state of each cell and ensuring that we explore all possible paths without repetition, we can significantly optimize our solution. Understanding the depth-first search strategy and the importance of backtracking in this context can help in tackling similar problems involving matrix traversal.

README for [Word Search (Leetcode #79)](https://blog.unwiredlearning.com/word-search) was compiled from the Unwired Learning Blog.