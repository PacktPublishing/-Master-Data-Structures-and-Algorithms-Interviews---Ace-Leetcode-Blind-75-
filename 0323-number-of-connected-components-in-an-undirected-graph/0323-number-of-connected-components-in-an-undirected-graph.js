class Solution {
    countComponents(n, edges) {
        // Initialize a graph represented as an adjacency list
        const graph = Array.from({ length: n }, () => []);
        for (const [u, v] of edges) {
            graph[u].push(v);
            graph[v].push(u);
        }

        const visited = new Array(n).fill(false);
        let components = 0;

        const dfs = (node) => {
            if (visited[node]) {
                return;
            }

            visited[node] = true;
            for (const neighbor of graph[node]) {
                dfs(neighbor);
            }
        };

        // Iterate through each node in the graph
        for (let i = 0; i < n; i++) {
            // If a node is unvisited, it's part of a new component
            if (!visited[i]) {
                dfs(i);
                components++;
            }
        }

        return components;
    }
}

//Question: https://www.lintcode.com/problem/3651/
//Blog: https://blog.unwiredlearning.com/number-of-connected-components-in-an-undirected-graph
