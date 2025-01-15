#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;
        if (heights.empty()) return result;

        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> pacificReachable(m, vector<bool>(n, false));
        vector<vector<bool>> atlanticReachable(m, vector<bool>(n, false));

        for (int i = 0; i < m; ++i) {
            dfs(heights, pacificReachable, i, 0);
            dfs(heights, atlanticReachable, i, n - 1);
        }

        for (int j = 0; j < n; ++j) {
            dfs(heights, pacificReachable, 0, j);
            dfs(heights, atlanticReachable, m - 1, j);
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (pacificReachable[i][j] && atlanticReachable[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        return result;
    }

private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& reachable, int row, int col) {
        reachable[row][col] = true;
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (auto& direction : directions) {
            int newRow = row + direction.first;
            int newCol = col + direction.second;
            if (newRow >= 0 && newRow < heights.size() && newCol >= 0 && newCol < heights[0].size() &&
                !reachable[newRow][newCol] && heights[newRow][newCol] >= heights[row][col]) {
                dfs(heights, reachable, newRow, newCol);
            }
        }
    }
};
