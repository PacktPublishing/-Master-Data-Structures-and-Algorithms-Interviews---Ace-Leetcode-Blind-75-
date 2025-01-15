class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        cycle = [False] * numCourses

        # Build graph with reversed logic
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def dfs(course):
            if cycle[course]:  # Cycle detected or already visited
                return False
            if graph[course] is None:  # No prerequisite for this course
                return True

            cycle[course] = True
            for prereq in graph[course]:
                if dfs(prereq) is False:
                    return False
            cycle[course] = False  # Reset for other paths
            graph[course] = []  # Clear prerequisites since it can be completed
            return True

        for i in range(numCourses):
            if dfs(i) is False:
                return False
        return True


#Question: https://leetcode.com/problems/course-schedule
#Blog: https://blog.unwiredlearning.com/course-schedule