# Number of Connected Components in an Undirected Graph (Leetcode 323)

In this blog, we will explore how to determine the number of connected components in an undirected graph. Understanding connected components is crucial for analyzing the structure of a graph and solving many graph-related problems. We'll start by breaking down the problem, discussing a brute force approach, and then dive into an efficient solution using Depth-First Search (DFS).

## Understanding the Problem Statement

The problem requires determining how many connected components are present in an undirected graph. Given a number of nodes (from `0` to `n-1`) and a list of edges between them, a connected component is a set of nodes where there is a path between any pair of nodes within that set. The graph may be made up of multiple disjoint subgraphs, and we want to identify how many such connected subgraphs exist.

For example, imagine a graph with `n = 5` nodes, with edges between nodes `0-1` and `2-3`. Here, there are three connected components: `0-1`, `2-3`, and `4` (node `4` is isolated).

## Brute Force Approach

A brute force approach to solving this problem would involve treating each node as the starting point and performing a traversal, such as Depth-First Search (DFS) or Breadth-First Search (BFS), to identify all reachable nodes. Each time we discover a new set of nodes that haven’t been visited before, we can count it as a new component.

The brute force approach would essentially involve starting a traversal from every node and keeping track of visited nodes. The time complexity for this approach, given the repeated traversals, can be quite high, making it inefficient for larger graphs.

## Hint to Solve the Problem Efficiently

The key to optimizing this problem is to avoid redundant traversals by keeping track of visited nodes efficiently. Instead of starting from each node multiple times, we can start from each unvisited node only, marking all reachable nodes in a single traversal. This way, we ensure that each node is visited exactly once, reducing the computational overhead.

## Efficient Solution

The provided code offers a more efficient solution by leveraging DFS to identify connected components. Here's a step-by-step breakdown:

1. **Graph Representation**: The graph is represented as an adjacency list, where each node points to a list of its neighbors. This allows efficient traversal.
    
    ```python
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    ```
    
2. **DFS Function**: The DFS function is defined to explore all nodes connected to a given starting node. It marks nodes as visited to prevent reprocessing.
    
    ```python
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for neighbor in graph[node]:
            dfs(neighbor)
    ```
    
3. **Counting Components**: We iterate over all nodes, and each time we find an unvisited node, we initiate a DFS traversal from that node, marking all reachable nodes. Each such initiation corresponds to finding a new connected component.
    
    ```python
    visited = [False] * n
    components = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1
    return components
    ```
    

This solution ensures that each node and edge is processed only once, resulting in improved efficiency.

## Time and Space Complexity

* **Time Complexity**: The time complexity of the efficient solution is **O(n + e)**, where `n` is the number of nodes and `e` is the number of edges. This is because each node is visited once, and each edge is traversed twice (once from each endpoint).
    
* **Space Complexity**: The space complexity is **O(n + e)** as well, due to the storage requirements of the adjacency list and the visited array. The recursion stack for DFS can also add to the space complexity in the worst case.
    

This efficient approach ensures that the graph is processed with minimal overhead, making it suitable for larger graphs.

## Conclusion

To summarize, determining the number of connected components in an undirected graph can be approached in multiple ways. The brute force method may be easy to understand but is inefficient for larger graphs. Using an optimized DFS approach allows us to solve the problem efficiently, with a time complexity of **O(n + e)**. Understanding these concepts and applying efficient graph traversal techniques can help solve a wide range of graph-related problems effectively.


README for [Number of Connected Components in an Undirected Graph (Leetcode 323)](https://blog.unwiredlearning.com/number-of-connected-components-in-an-undirected-graph) was compiled from the Unwired Learning Blog.