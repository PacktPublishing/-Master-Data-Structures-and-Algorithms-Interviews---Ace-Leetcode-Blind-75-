#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    bool validTree(int n, std::vector<std::vector<int>>& edges) {
        // Check for the necessary condition of a tree (n-1 edges)
        if (edges.size() != n - 1) {
            return false;
        }

        // Create an adjacency list
        std::unordered_map<int, std::vector<int>> graph;
        for (int i = 0; i < n; ++i) {
            graph[i] = std::vector<int>();
        }
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        std::unordered_set<int> visited;

        std::function<bool(int, int)> dfs = [&](int node, int parent) {
            if (visited.count(node)) {
                return false;
            }
            visited.insert(node);

            for (int neighbor : graph[node]) {
                if (neighbor == parent) {
                    continue;
                }
                if (!dfs(neighbor, node)) {
                    return false;
                }
            }

            return true;
        };

        // Start DFS from node 0; Check if it's fully connected and has no cycle
        return dfs(0, -1) && visited.size() == n;
    }
};

//Question: https://www.lintcode.com/problem/178
//Blog: https://blog.unwiredlearning.com/graph-valid-tree
