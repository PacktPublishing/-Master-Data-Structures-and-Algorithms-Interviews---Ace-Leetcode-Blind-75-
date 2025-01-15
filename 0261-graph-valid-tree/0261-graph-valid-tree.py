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


#Question: https://www.lintcode.com/problem/178
#Blog: https://blog.unwiredlearning.com/graph-valid-tree