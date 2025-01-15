"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

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
            # "Dequeue" operation using list pop from the front (index 0)
            current_node = queue.pop(0)
            
            for neighbor in current_node.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone and store the neighbor if it's not yet cloned
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    # Enqueue the neighbor
                    queue.append(neighbor)
                
                # Add the clone of the neighbor to the current node's clone neighbors list
                cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])
        
        return cloned_nodes[node]


#Question: https://leetcode.com/problems/clone-graph
#Blog: https://blog.unwiredlearning.com/clone-graph