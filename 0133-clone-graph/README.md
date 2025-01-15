# Clone Graph (Leetcode #133)

The Clone Graph problem is a popular graph-related question often asked in technical interviews and coding assessments. It tests your understanding of graph traversal techniques and your ability to create independent copies of complex data structures. In this blog, we'll delve into the problem, explore a brute force approach, and then provide an efficient solution to help you understand how to tackle this challenge effectively.

## Understanding the Problem Statement

The problem presented in LeetCode 133, **Clone Graph**, is about copying an entire graph. Given a reference to a node in an undirected graph, the task is to return a deep copy of the graph. Each node has a value and a list of neighbors. The graph might be disconnected, and there could be cycles, which means a node can be its own neighbor or part of a cycle.

In simple terms, you are provided with a node that represents a complex network, and your job is to create an identical network but as an independent copy. The challenge comes from preserving the relationships between nodes while ensuring none of the original references are reused.

## Brute Force Approach

The brute force approach to solving this problem involves **DFS (Depth First Search)** or **BFS (Breadth First Search)** with naive copying. You could start by visiting each node and copying its value. But, as nodes have references to other nodes, the naive approach would end up in an endless cycle if there are loops, or cause incorrect connections in the case of shared neighbors. This naive implementation lacks the mechanism to keep track of nodes that have already been cloned, causing inefficiencies and logical issues.

## Hint to Solve the Problem Efficiently

A successful approach involves using a **HashMap** (or dictionary) to keep track of already cloned nodes. This way, you can ensure that nodes are only cloned once, and all relationships are maintained. Think of it as a mapping of nodes in the original graph to their corresponding clones in the new graph.

## Efficient Solution

Below is an efficient solution based on **Breadth First Search (BFS)**:

The given solution uses a dictionary called `cloned_nodes` to map each original node to its corresponding cloned node. It begins by checking if the provided node is `None`, in which case, it returns `None` (as there is nothing to clone). The algorithm proceeds as follows:

1. **Initialization**: A dictionary called `cloned_nodes` is created to store the mapping of original nodes to their clones. The input node is cloned first, and both the original node and its clone are placed in the dictionary.
    
2. **Queue Setup**: A queue is initialized with the original node to help with the BFS traversal.
    
3. **BFS Traversal**: During traversal, for every node in the queue, its neighbors are iterated over.
    
    * If a neighbor is not yet cloned, it is cloned and added to the `cloned_nodes` dictionary and the queue for future exploration.
        
    * The neighbor is added to the neighbors list of the cloned version of the current node.
        
4. **Returning the Result**: Finally, the clone of the starting node is returned, which contains references to all other cloned nodes, thus representing the complete deep copy of the original graph.
    

Here is the efficient solution code for reference:

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
    
        # Mapping from original to cloned node
        cloned_nodes = {}
        
        # Initialize the "queue" with the first node
        queue = [node]
        
        # Clone the first node and add it to the cloned nodes map
        cloned_nodes[node] = Node(node.val)
        
        # BFS traversal
        while queue:
            current_node = queue.pop(0)
            
            for neighbor in current_node.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone and store the neighbor if it's not yet cloned
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add the clone of the neighbor to the current node's clone neighbors list
                cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])
        
        return cloned_nodes[node]
```

## Time and Space Complexity

The **Time Complexity** of the above solution is **O(N + M)**, where **N** is the number of nodes and **M** is the number of edges. This is because each node and edge is processed exactly once during the BFS traversal.

The **Space Complexity** is also **O(N)**, as we need extra space for storing cloned nodes in the dictionary and for maintaining the queue during BFS. The number of cloned nodes is proportional to the number of original nodes, and the queue holds references to nodes that need to be processed.

Using BFS and the hashmap-based tracking ensures we efficiently maintain relationships while avoiding repeated cloning, which makes this solution robust and performant for any graph structure, whether it has cycles, disconnected parts, or complex neighbor relationships.

## Conclusion

The Clone Graph problem is an excellent way to practice graph traversal techniques and understand how to handle complex data structures involving references. By using a BFS approach combined with a HashMap to keep track of cloned nodes, we can efficiently create a deep copy of any undirected graph. This solution ensures that all relationships are preserved while avoiding unnecessary re-cloning, making it suitable for even complex and cyclic graphs. Practicing problems like this will help you build a strong foundation in graph algorithms and data structure manipulation, which are critical skills for technical interviews and real-world software development.


README for [Clone Graph (Leetcode #133)](https://blog.unwiredlearning.com/clone-graph) was compiled from the Unwired Learning Blog.