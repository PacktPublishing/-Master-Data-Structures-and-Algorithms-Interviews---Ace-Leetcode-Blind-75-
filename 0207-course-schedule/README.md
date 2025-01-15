# Course Schedule (Leetcode 207)

The "Course Schedule" problem is a popular challenge that tests your understanding of graph traversal and cycle detection. Given a number of courses and their prerequisites, the task is to determine if it is possible to complete all the courses. This blog will walk you through a brute force approach, provide a hint for an optimized solution, and finally present an efficient method to solve the problem.

## Understanding the Problem Statement

The "Course Schedule" problem on LeetCode, numbered 207, is a classic problem that asks if you can finish all the courses given their prerequisites. Essentially, you are given a list of courses (represented by numbers) and a list of pairs that specify the prerequisites for these courses. The goal is to determine whether it is possible to complete all the courses while respecting the prerequisites. This is very much like finding whether it is possible to complete a list of tasks, each of which depends on the completion of other tasks.

In more technical terms, the question asks if there is a cycle in the dependency graph of courses. If a cycle exists, it means that there is no possible order to take all the courses, and the answer would be "False." Otherwise, the answer is "True."

## Brute Force Approach

A common brute force approach to solve the problem involves trying all possible orders of taking the courses and checking whether any sequence satisfies all the prerequisites. One way to do this is to perform a topological sort on all possible orders of courses to check if such an order exists that fulfills all the conditions. However, this approach is highly inefficient due to the factorial number of possibilities, making it impractical for large inputs. This is due to the fact that topological sorting in a brute force way can take too much time and space, especially when the graph is complex and contains many nodes (courses).

## Hint to Solve the Problem Efficiently

Instead of trying all possible orders, think about using Depth-First Search (DFS) to detect if there is a cycle in the graph. The key is to use DFS to traverse through each course and its prerequisites. If you encounter a course that is already in the current traversal path, then you have detected a cycle, which means it is not possible to finish all the courses. The provided code uses a clever approach to build the graph and checks for cycles efficiently, which avoids the need for an exhaustive search.

## Efficient Solution

The efficient solution uses Depth-First Search (DFS) to detect cycles in the course prerequisite graph. Let's walk through the provided code:

1. **Graph Representation**: The graph is represented using an adjacency list where each course points to its prerequisites.
    
    ```python
    graph = [[] for _ in range(numCourses)]
    ```
    
    Here, each index in the `graph` list represents a course, and the value is a list of other courses that are prerequisites for the current course.
    
2. **Building the Graph**: The graph is built in reverse order, where each course points to its prerequisites.
    
    ```python
    for pair in prerequisites:
        graph[pair[0]].append(pair[1])
    ```
    
3. **Cycle Detection with DFS**: A `cycle` array is used to keep track of nodes currently in the traversal path.
    
    ```python
    cycle = [False] * numCourses
    ```
    
    The DFS function is used to traverse each course. If the current course is already in the cycle (visited again in the same path), it returns `False` indicating a cycle.
    
    ```python
    def dfs(course):
        if cycle[course]:
            return False
        if graph[course] is None:
            return True
        
        cycle[course] = True
        for prereq in graph[course]:
            if dfs(prereq) is False:
                return False
        cycle[course] = False
        graph[course] = []
        return True
    ```
    
    * If a cycle is detected, `False` is returned, indicating it is not possible to finish all courses.
        
    * If no cycle is detected, the course's prerequisites are marked as completed by setting `graph[course] = []`.
        
4. **Checking All Courses**: Finally, we iterate through all courses to ensure that each one can be completed without a cycle.
    
    ```python
    for i in range(numCourses):
        if dfs(i) is False:
            return False
    return True
    ```
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of the solution is `O(V + E)`, where `V` is the number of courses (`numCourses`) and `E` is the number of dependencies (prerequisites). This is because each node and edge is processed once in the DFS traversal.
    
* **Space Complexity**: The space complexity is also `O(V + E)` due to the storage requirements of the graph and the recursion stack used by the DFS. The `cycle` array and the graph representation both take `O(V + E)` space.
    

This approach is efficient because it processes each course and its prerequisites in a linear fashion, avoiding the combinatorial explosion of the brute force approach.

## Conclusion

The "Course Schedule" problem is a great example of how graph traversal techniques like DFS can be used to solve practical problems involving dependencies. By detecting cycles in the graph representation of courses and their prerequisites, we can efficiently determine whether it is possible to complete all courses. This problem helps build an understanding of cycle detection, graph representation, and recursive thinking, which are crucial skills for tackling complex graph-related problems.


README for [Course Schedule (Leetcode 207)](https://blog.unwiredlearning.com/course-schedule) was compiled from the Unwired Learning Blog.