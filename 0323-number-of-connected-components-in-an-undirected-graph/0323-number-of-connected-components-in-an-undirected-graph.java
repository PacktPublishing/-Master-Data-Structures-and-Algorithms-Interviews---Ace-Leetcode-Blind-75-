import java.util.*;

class Solution {
    public int countComponents(int n, int[][] edges) {
        // Initialize a graph represented as an adjacency list
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        // Populate the graph with the given edges
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int components = 0;

        // DFS function
        void dfs(int node) {
            if (visited[node]) {
                return;
            }

            visited[node] = true;
            for (int neighbor : graph.get(node)) {
                dfs(neighbor);
            }
        }

        // Iterate through each node in the graph
        for (int i = 0; i < n; i++) {
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
