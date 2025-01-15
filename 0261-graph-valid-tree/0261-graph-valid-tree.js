class Solution {
    validTree(n, edges) {
        // Check for the necessary condition of a tree (n-1 edges)
        if (edges.length !== n - 1) {
            return false;
        }

        // Create an adjacency list
        const graph = Array.from({ length: n }, () => []);
        for (const [u, v] of edges) {
            graph[u].push(v);
            graph[v].push(u);
        }

        const visited = new Set();

        const dfs = (node, parent) => {
            if (visited.has(node)) {
                return false;
            }
            visited.add(node);

            for (const neighbor of graph[node]) {
                if (neighbor === parent) {
                    continue;
                }
                if (!dfs(neighbor, node)) {
                    return false;
                }
            }

            return true;
        };

        // Start DFS from node 0; Check if it's fully connected and has no cycle
        return dfs(0, -1) && visited.size === n;
    }
}

//Question: https://www.lintcode.com/problem/178
//Blog: https://blog.unwiredlearning.com/graph-valid-tree
