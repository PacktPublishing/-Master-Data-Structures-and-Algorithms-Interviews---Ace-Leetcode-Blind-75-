#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int countComponents(int n, std::vector<std::vector<int>>& edges) {
        // Initialize a graph represented as an adjacency list
        std::unordered_map<int, std::vector<int>> graph;
        for (int i = 0; i < n; ++i) {
            graph[i] = std::vector<int>();
        }

        // Populate the graph with the given edges
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        std::vector<bool> visited(n, false);
        int components = 0;

        // DFS function
        std::function<void(int)> dfs = [&](int node) {
            if (visited[node]) {
                return;
            }

            visited[node] = true;
            for (int neighbor : graph[node]) {
                dfs(neighbor);
            }
        };

        // Iterate through each node in the graph
        for (int i = 0; i < n; ++i) {
            // If a node is unvisited, it's part of a new component
            if (!visited[i]) {
                dfs(i);
                components++;
            }
        }

        return components;
    }
};

//Question: https://www.lintcode.com/problem/3651/
//Blog: https://blog.unwiredlearning.com/number-of-connected-components-in-an-undirected-graph
