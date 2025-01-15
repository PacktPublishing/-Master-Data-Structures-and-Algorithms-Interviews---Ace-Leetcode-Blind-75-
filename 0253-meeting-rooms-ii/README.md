# Meeting Rooms II (Leetcode #253)

Managing meeting schedules in a busy office can feel like a puzzle. Today, we'll explore how to solve one such puzzle using a problem from LeetCode: **Meeting Rooms II**. This problem is a classic example of optimal resource allocation in a constrained environment, and we will look into the brute force approach as well as a more efficient method for solving it.

## Understanding the Problem Statement

Imagine that you're given a list of meeting intervals with their start and end times, and you need to determine the minimum number of meeting rooms required to hold all the meetings. Each meeting has a start and end time, and meetings can overlap. Your task is to find out how many meeting rooms are needed at the peak.

For instance, if the input is:

```python
[[0, 30], [5, 10], [15, 20]]
```

The output should be `2`, as two rooms are needed to accommodate overlapping meetings.

## Brute Force Approach

A common way to approach this problem is to iterate through all possible combinations of meeting intervals and check for overlaps. For every meeting, you can iterate through all the other meetings and count how many overlap with the current one. This approach is not very efficient, as it involves nested loops that have a time complexity of `O(n^2)`. This is particularly inefficient when dealing with a large number of meetings, as every meeting is checked against every other one.

The brute force approach gives you an idea of what needs to be done—managing overlaps—but it's not suitable when performance is critical.

## Hint to Solve the Problem Efficiently

Instead of comparing every meeting with all others, consider sorting the meeting times and using a greedy approach to manage the allocation. Think of splitting the meetings into their start and end times and using pointers to track the usage of meeting rooms.

## Efficient Solution

The provided solution uses a technique involving sorting both the start and end times of the meetings:

```python
# Efficient Solution

def minMeetingRooms(intervals):
    # Separate and sort start and end times
    start_times = sorted(interval.start for interval in intervals)
    end_times = sorted(interval.end for interval in intervals)

    start_pointer, end_pointer = 0, 0
    used_rooms = 0
    max_rooms = 0

    # Iterate over start times
    while start_pointer < len(intervals):
        if start_times[start_pointer] < end_times[end_pointer]:
            # A new room is needed
            used_rooms += 1
            start_pointer += 1
        else:
            # A room is freed up
            used_rooms -= 1
            end_pointer += 1
        
        # Update the maximum number of rooms needed
        max_rooms = max(max_rooms, used_rooms)

    return max_rooms
```

In this approach, both the start and end times are sorted separately. Two pointers are used to keep track of the current meeting that is starting and the meeting that is ending. As we iterate through the sorted start times, we either need a new room (if a meeting starts before another ends), or we release a room when the current meeting ends.

**How This Works**

* **Step 1:** Sort the start and end times.
    
* **Step 2:** Use pointers to iterate through the start and end arrays.
    
* **Step 3:** Track the number of rooms being used. Whenever a meeting starts before another ends, a room is allocated; otherwise, a room is freed.
    
* **Step 4:** Update the maximum number of rooms needed during this process.
    

This approach allows you to efficiently manage room allocation without explicitly checking every pair of meetings.

## Time and Space Complexity

* **Time Complexity:** Sorting both the start and end times takes `O(n log n)` time. Iterating over the start times and end times has a linear complexity of `O(n)`. Hence, the overall time complexity is `O(n log n)`, which is optimal for this type of problem.
    
* **Space Complexity:** The space complexity is `O(n)` because we store the start and end times in separate arrays. There is also additional space required for sorting, but it remains efficient in practice.
    

## Conclusion

The 'Meeting Rooms II' problem helps illustrate the importance of an optimal approach in situations where resources are constrained. The brute force method is a good conceptual starting point, but leveraging sorted data and an efficient tracking mechanism allows for significantly better performance. Sorting start and end times and managing with pointers is a smart and clean way to solve this problem. Consider using these principles when faced with similar resource allocation challenges.

README for [Meeting Rooms II (Leetcode #253)](https://blog.unwiredlearning.com/meeting-rooms-ii) was compiled from the Unwired Learning Blog.