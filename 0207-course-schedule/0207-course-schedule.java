import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        boolean[] cycle = new boolean[numCourses];

        // Build graph with reversed logic
        for (int[] pair : prerequisites) {
            graph.get(pair[0]).add(pair[1]);
        }

        // DFS function to detect cycle
        boolean dfs(int course) {
            if (cycle[course]) {  // Cycle detected or already visited
                return false;
            }
            if (graph.get(course).isEmpty()) {  // No prerequisite for this course
                return true;
            }

            cycle[course] = true;
            for (int prereq : graph.get(course)) {
                if (!dfs(prereq)) {
                    return false;
                }
            }
            cycle[course] = false;  // Reset for other paths
            graph.get(course).clear();  // Clear prerequisites since it can be completed
            return true;
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return false;
            }
        }
        return true;
    }
}

//Question: https://leetcode.com/problems/course-schedule
//Blog: https://blog.unwiredlearning.com/course-schedule
