# Graph Valid Tree (Leetcode 261)

In this blog, we will explore the problem of determining whether a given graph forms a valid tree, commonly known as Leetcode problem 261. We will discuss the problem statement, a brute force approach, provide hints for an efficient solution, and break down the optimal solution with detailed complexity analysis. By the end of this blog, you will have a clear understanding of how to solve this problem efficiently.

## Understanding the Problem Statement

The problem "Graph Valid Tree" is about determining whether a given graph represents a valid tree. You are provided with `n` nodes labeled from `0` to `n-1` and a list of edges connecting them. The goal is to determine if these nodes and edges form a valid tree.

A graph is considered a tree if:

1. All nodes are connected (there is a path between any two nodes).
    
2. The graph has no cycles.
    
3. The number of edges should be exactly `n - 1`, which is a necessary condition for a tree.
    

In this problem, the input consists of:

* `n` - an integer representing the number of nodes.
    
* `edges` - a list of pairs representing the connections between nodes.
    

The task is to return `True` if the graph forms a valid tree, otherwise `False`.

## Brute Force Approach

A brute force approach to solve this problem could involve checking if the graph is both fully connected and contains no cycles. You could iterate through every node and check for connectivity using multiple traversal methods like Breadth-First Search (BFS) or Depth-First Search (DFS), while also checking for cycles.

However, a key limitation of such an approach is its inefficiency, particularly in cycle detection, as you might end up visiting nodes multiple times and creating unnecessary overhead.

## Hint to Solve the Problem Efficiently

The efficient solution involves using both a DFS and a key observation about the structure of trees: a valid tree must have exactly `n - 1` edges. If the number of edges is not `n - 1`, it is impossible for the graph to be a tree. You can use an adjacency list to represent the graph, and a DFS traversal to ensure there are no cycles and that all nodes are connected.

## Efficient Solution

Below is the efficient solution code that was provided:

```python
    def validTree(n, edges):
        # Check for the necessary condition of a tree (n-1 edges)
        if len(edges) != n - 1:  
            return False
        
        # Create an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in graph[node]:
                # Ignore the edge leading back to the parent
                if neighbor == parent:  
                    continue
                
                # Attempt to visit each neighboring node using DFS.
                path_is_clear = dfs(neighbor, node)
                if path_is_clear is False:
                    return False
            
            return True
        
        # Start DFS from node 0; Check if it's fully connected and has no cycle
        return dfs(0, -1) and len(visited) == n
```

**Explanation of the Solution**

1. **Edge Count Check**: The first step is to verify if the number of edges is equal to `n - 1`. If not, it is not possible for the graph to be a valid tree.
    
2. **Graph Representation**: The graph is represented using an adjacency list, where each node points to its neighbors. This is efficient for traversal.
    
3. **DFS for Connectivity and Cycle Detection**: The `dfs` function is used to traverse the graph.
    
    * It checks if a node has already been visited, which indicates a cycle.
        
    * The DFS is initiated from node `0`, and we ignore the edge that leads back to the parent.
        
    * During the traversal, if a cycle is detected or if any node is unreachable, the function returns `False`.
        
4. **Final Validation**: Finally, the function returns `True` only if all nodes are visited (i.e., the number of visited nodes equals `n`). This ensures the graph is fully connected and free of cycles.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity is `O(N + E)`, where `N` is the number of nodes and `E` is the number of edges. This is because we traverse all nodes and edges during the DFS.
    
* **Space Complexity**: The space complexity is `O(N)` due to the adjacency list and the `visited` set. The recursion stack for DFS also takes up space in the worst case, which is proportional to `O(N)` in the case of a fully connected graph.
    

## Conclusion

In conclusion, solving the "Graph Valid Tree" problem requires understanding the fundamental properties of a tree, such as the edge count and connectivity. By leveraging depth-first search (DFS) and an adjacency list, we can efficiently determine if the given graph is a valid tree. Remember, ensuring that the graph has exactly `n - 1` edges is the first critical step, followed by checking for cycles and full connectivity. This solution provides an optimal way to solve the problem within acceptable time and space complexity limits.


README for [Graph Valid Tree (Leetcode 261)](https://blog.unwiredlearning.com/graph-valid-tree) was compiled from the Unwired Learning Blog.