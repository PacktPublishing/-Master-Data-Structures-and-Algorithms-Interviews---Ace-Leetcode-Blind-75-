# Find Median from Data Stream (Leetcode #295)

In this blog, we will discuss the brute force approach, provide hints for solving the problem efficiently, and dive into an optimal solution using a combination of Trie and DFS.

## Understanding the Problem Statement

Word Search II (Leetcode 212) is a popular backtracking problem where you're given a 2D board of letters and a list of words. The goal is to find all words from the list that exist in the board, where each word must be formed by sequentially adjacent letters (either horizontally or vertically), without reusing the same cell twice.

## Brute Force Approach

In the brute force approach, you would start by iterating over each cell in the board and attempting to find each word starting from that particular cell. This typically involves exploring all possible directions to try and match each character of a word. While easy to understand, this approach suffers from severe inefficiency as the same searches are repeated for each word, resulting in an exponential time complexity. As the board and word list grow, the brute force method becomes impractical due to high computational costs.

## Hint to Solve the Problem Efficiently

The provided solution involves using a **Trie** (prefix tree) to optimize the search process. A Trie is built to efficiently store and look up the words from the given list, which helps in reducing redundant searches during the depth-first traversal of the board. The combination of the Trie and Depth-First Search (DFS) drastically improves the performance, especially when dealing with large boards and numerous words.

## Efficient Solution

To efficiently solve the problem, we combine **DFS** and a **Trie** to minimize redundant computations and speed up the word search. Below is the efficient solution from the provided code:

1. **Building the Trie**: The `buildTrie` function takes the given list of words and constructs a Trie. Each node of the Trie represents a character, and the Trie as a whole represents all the words. This allows for quick lookups when attempting to match a word starting from any cell on the board.
    
2. **DFS for Word Search**: The `dfs` function performs depth-first search on the board, starting from any character that matches the root of the Trie. As each character is found, it moves deeper into the Trie, and ultimately, if a word is found, it is added to the result.
    
3. **Marking Visited Cells**: During the DFS, cells are marked as visited by temporarily changing their value. This avoids revisiting cells within the same path. After the DFS is complete, the cells are restored to their original values to maintain board integrity.
    
4. **Avoiding Duplicates**: Once a word is found, it is added to the result set and marked as found in the Trie to avoid duplicate entries in the final result.
    

Here's a summary of the approach used:

* **Trie Construction**: Efficiently represents words for quick lookup.
    
* **DFS Search**: Explores possible words starting from each board cell, backtracking as needed.
    
* **Result Set**: Keeps track of found words to avoid duplicates.
    

## Time and Space Complexity

**Time Complexity**: The solution has an average complexity of **O(M × N × 4^L)**, where **M** is the number of rows, **N** is the number of columns in the board, and **L** is the length of the longest word. The Trie lookup and pruning of search space help reduce unnecessary computations, making the solution much more efficient compared to a brute-force search.

**Space Complexity**: The space complexity is **O(W × L + M × N)**, where **W** is the number of words and **L** is the average length of the words. This includes space for storing the Trie as well as the recursion stack used during the DFS traversal. While the Trie structure can be memory-intensive, it is a necessary trade-off for the significant speed-up in search performance.

## Conclusion

Word Search II is a challenging problem that requires an optimized approach to handle large boards and multiple words efficiently. By combining the Trie data structure with depth-first search, we can significantly reduce redundant operations and speed up the word search process. This efficient solution not only highlights the power of combining different algorithms but also serves as a great exercise in improving the time complexity of typical brute-force approaches. With a solid understanding of Trie and DFS, solving complex word search problems becomes much more manageable.


README for [Find Median from Data Stream (Leetcode #295)](https://blog.unwiredlearning.com/find-median-from-data-stream) was compiled from the Unwired Learning Blog.