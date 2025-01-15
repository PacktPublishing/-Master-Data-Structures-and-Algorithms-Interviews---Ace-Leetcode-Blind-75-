# Alien Dictionary (Leetcode 269)

The Alien Dictionary problem is a challenging yet fascinating problem that involves determining the order of characters in an alien language based on the lexicographical order of words provided. In this blog, we will walk through the problem statement, explore a brute force approach, provide a hint for solving it efficiently, and ultimately dive into an optimal solution using graph theory.

## Understanding the Problem Statement

The Alien Dictionary problem presents a list of words from an unknown language, and your task is to determine the alphabet order of the characters in that language. You are given an ordered list of words and must derive the correct order of letters based on the differences between consecutive words.

The catch is that, since the words are sorted lexicographically in the alien language, you must infer the relative order of characters based on the provided list. Essentially, it’s similar to deriving an ordering for the characters that respect their relationships in a given dictionary.

The problem is analogous to creating a topological order for nodes in a graph, where nodes represent letters and directed edges represent their relative order.

## Brute Force Approach

A common brute-force approach would be to generate every possible permutation of the characters in the given list of words and check if each permutation satisfies the ordering constraints derived from the word list. This involves generating all possible character orders, then verifying if each order respects the given order in the words list. However, this approach is computationally impractical because the number of permutations grows factorially with the number of distinct characters, making it extremely inefficient for larger inputs.

## Hint to Solve the Problem Efficiently

Instead of generating all possible orders, think of this problem as a graph traversal problem. Each character in the language can be thought of as a node in a directed graph, and edges represent the precedence between characters based on the order of the given words. You can perform a Depth First Search (DFS) on the graph to obtain a valid character order while detecting any cycles that would make the ordering impossible.

## Efficient Solution

The efficient solution involves breaking down the problem into three main steps:

1. **Create the Graph**: Iterate through the list of words and compare adjacent words to determine character precedence. Each character is a node, and an edge between two nodes (characters) represents that one character must come before the other.
    
    ```python
    adj = {c: set() for word in words for c in word}
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        minLen = min(len(word1), len(word2))
        
        # Handle the case where order is impossible.
        if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
            return ""  
        
        for j in range(minLen):
            if word1[j] != word2[j]:
                adj[word1[j]].add(word2[j])
                break
    ```
    
2. **Detect Cycles and Perform DFS**: To determine a valid ordering, perform a Depth First Search (DFS) on each character. During the DFS, track visited nodes to detect cycles, as cycles imply an impossible ordering. Use a dictionary to mark each node as visited (False for visiting, True for processed).
    
    ```python
    visited = {}  # False = visited but not processed, True = processed.
    order = []
    
    def dfs(c):
        if c in visited:
            return visited[c]  # If True, no cycle; if False, cycle detected.
        visited[c] = False
        for nei in adj[c]:
            if dfs(nei) == False:
                return False  # Cycle detected.
        visited[c] = True
        order.append(c)
        return True
    
    for c in adj:
        if c not in visited:
            if not dfs(c):
                return ""  # Cycle detected.
    ```
    
3. **Return the Result**: After the DFS traversal, the characters are appended in reverse post-order. Thus, we reverse the list to get the correct character order.
    
    ```python
    return "".join(order[::-1])
    ```
    

## Time and Space Complexity

* **Time Complexity**: The solution involves creating a graph with `O(N * M)` complexity, where `N` is the number of words and `M` is the average length of the words. Additionally, the DFS traversal runs in `O(V + E)` time, where `V` is the number of vertices (distinct characters) and `E` is the number of edges (precedence relations). Overall, the time complexity is `O(N * M + V + E)`, which is efficient compared to the brute-force approach.
    
* **Space Complexity**: The space complexity is `O(V + E)` due to storing the graph representation and the visited dictionary. The graph stores each character as a node and the relations as edges, resulting in linear space usage relative to the input size.
    

## Conclusion

The Alien Dictionary problem is a great way to understand graph traversal concepts and topological sorting. By representing characters as nodes and their relationships as directed edges, we can solve the problem using an efficient graph-based approach. Although the brute-force solution is impractical, the DFS-based solution provides a clear path to determining the character order while handling edge cases like cycles. Understanding these fundamental graph algorithms can be highly beneficial for tackling a wide range of similar problems in computer science.


README for [Alien Dictionary (Leetcode 269)](https://blog.unwiredlearning.com/alien-dictionary) was compiled from the Unwired Learning Blog.