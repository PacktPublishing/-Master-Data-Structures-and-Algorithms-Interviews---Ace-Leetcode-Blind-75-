import java.util.*;

class Solution {
    public boolean validTree(int n, int[][] edges) {
        // Check for the necessary condition of a tree (n-1 edges)
        if (edges.length != n - 1) {
            return false;
        }

        // Create an adjacency list
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();

        // DFS function to check for cycles and connectivity
        boolean dfs(int node, int parent) {
            if (visited.contains(node)) {
                return false;
            }
            visited.add(node);

            for (int neighbor : graph.get(node)) {
                if (neighbor == parent) {
                    continue;
                }
                if (!dfs(neighbor, node)) {
                    return false;
                }
            }

            return true;
        }

        // Start DFS from node 0; Check if it's fully connected and has no cycle
        return dfs(0, -1) && visited.size() == n;
    }
}

//Question: https://www.lintcode.com/problem/178
//Blog: https://blog.unwiredlearning.com/graph-valid-tree
