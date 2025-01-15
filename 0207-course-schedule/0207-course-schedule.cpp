#include <vector>
#include <functional>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> graph(numCourses);
        std::vector<bool> cycle(numCourses, false);

        // Build graph with reversed logic
        for (const auto& pair : prerequisites) {
            graph[pair[0]].push_back(pair[1]);
        }

        // DFS function to detect cycle
        std::function<bool(int)> dfs = [&](int course) {
            if (cycle[course]) {  // Cycle detected or already visited
                return false;
            }
            if (graph[course].empty()) {  // No prerequisite for this course
                return true;
            }

            cycle[course] = true;
            for (int prereq : graph[course]) {
                if (!dfs(prereq)) {
                    return false;
                }
            }
            cycle[course] = false;  // Reset for other paths
            graph[course].clear();  // Clear prerequisites since it can be completed
            return true;
        };

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return false;
            }
        }
        return true;
    }
};

//Question: https://leetcode.com/problems/course-schedule
//Blog: https://blog.unwiredlearning.com/course-schedule
