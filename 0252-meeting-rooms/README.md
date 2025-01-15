# Meeting Rooms (Leetcode #252)

The "Meeting Rooms" problem is a classic interview question that tests your understanding of intervals, sorting, and detecting overlaps. In this blog, we will walk through this problem in detail, explore a common brute force approach, provide hints, and eventually discuss an efficient solution, justified by time and space complexity. Let's get started!

## Understanding the Problem Statement

You are given an array of meeting time intervals where each interval is represented as `[start, end]`. You need to determine if a person can attend all the meetings without any overlap. Essentially, you are asked whether there are any overlaps between the meetings.

For example:

```python
Input: [[0, 30], [5, 10], [15, 20]]
Output: False
```

In this example, meetings overlap, so the output is `False`. If all meetings were non-overlapping, the output would be `True`.

## Brute Force Approach

A common brute force approach involves comparing each pair of meetings to see if there is any overlap. To do this, you could iterate through all intervals and for each interval, compare it with every other interval to check if they overlap.

Pseudo-code for brute force solution:

```python
for i in range(len(intervals)):
    for j in range(i + 1, len(intervals)):
        if intervals[i][1] > intervals[j][0] and intervals[i][0] < intervals[j][1]:
            return False
return True
```

This solution checks every possible pair of intervals for overlaps, which is inefficient as it has a time complexity of `O(N^2)`, where `N` is the number of intervals.

## Hint to Solve the Problem Efficiently

To solve this problem more efficiently, think about sorting the intervals by their start time. Once sorted, a single pass through the intervals is enough to check if any two consecutive meetings overlap. This way, you don't need to compare every pair, making the solution significantly faster.

## Efficient Solution

The efficient approach involves first sorting the intervals based on the start times and then iterating through the sorted list to check for overlaps. Here is the Python code for the solution, based on the provided code:

```python
# Function to determine if a person can attend all meetings
def can_attend_meetings(intervals):
    # Step 1: Sort the intervals by start time
    intervals.sort()
    
    # Step 2: Check for any overlap between consecutive meetings
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
            
    return True
```

In this solution, we first sort the intervals by their starting times. Then, we iterate through the sorted intervals to check if the start time of the current meeting is earlier than the end time of the previous meeting. If it is, we return `False`, indicating there is an overlap. If no overlaps are found, we return `True`.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(N log N)` due to the sorting step, where `N` is the number of intervals. The subsequent iteration through the intervals has a time complexity of `O(N)`, making the overall complexity `O(N log N)`.
    
* **Space Complexity**: The space complexity of this solution is `O(1)` if the sorting is done in-place. Otherwise, it is `O(N)` if the sorting requires additional space.
    

## Conclusion

The "Meeting Rooms" problem is a great example to illustrate the power of sorting in simplifying interval problems. While the brute force approach has quadratic complexity, sorting allows us to reduce the number of comparisons, making the solution much more efficient. By sorting and then performing a single scan, we can determine if a person can attend all the meetings without overlap, achieving an optimal solution with `O(N log N)` time complexity. Practice and master this approach, as similar interval-based problems often appear in technical interviews.

README for [Meeting Rooms (Leetcode #252)](https://blog.unwiredlearning.com/meeting-rooms) was compiled from the Unwired Learning Blog.