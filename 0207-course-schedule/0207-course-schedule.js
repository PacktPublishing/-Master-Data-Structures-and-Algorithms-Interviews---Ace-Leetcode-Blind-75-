class Solution {
    canFinish(numCourses, prerequisites) {
        const graph = Array.from({ length: numCourses }, () => []);
        const cycle = new Array(numCourses).fill(false);

        // Build graph with reversed logic
        for (const [course, prereq] of prerequisites) {
            graph[course].push(prereq);
        }

        const dfs = (course) => {
            if (cycle[course]) {  // Cycle detected or already visited
                return false;
            }
            if (graph[course].length === 0) {  // No prerequisite for this course
                return true;
            }

            cycle[course] = true;
            for (const prereq of graph[course]) {
                if (!dfs(prereq)) {
                    return false;
                }
            }
            cycle[course] = false;  // Reset for other paths
            graph[course] = [];  // Clear prerequisites since it can be completed
            return true;
        };

        for (let i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return false;
            }
        }
        return true;
    }
}

//Question: https://leetcode.com/problems/course-schedule
//Blog: https://blog.unwiredlearning.com/course-schedule
