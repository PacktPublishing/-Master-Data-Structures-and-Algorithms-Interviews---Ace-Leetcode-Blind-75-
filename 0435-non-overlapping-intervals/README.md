# Non-overlapping Intervals (Leetcode #435)

In this blog, we'll explore an interesting problem from LeetCode - the **435\. Non-overlapping Intervals** problem. We'll start by understanding the problem statement, look at a common brute force solution, and discuss a more efficient approach along with an analysis of its time and space complexity. If you've been practicing interval problems and looking to improve your greedy algorithm skills, this is the perfect problem to learn from.

## Understanding the Problem Statement

The **Non-overlapping Intervals** problem asks us to find the minimum number of intervals to remove in order to make the rest of the intervals non-overlapping. Each interval is given as an array of two integers, where the first represents the start and the second represents the end. The objective is to eliminate the overlapping intervals while keeping as many intervals as possible.

For example, consider these intervals: **\[\[1,3\], \[2,4\], \[3,5\]\]**. The goal is to remove the fewest number of intervals so that no two intervals overlap. In this case, we can remove either **\[1,3\]** or **\[2,4\]** to avoid overlap, which means the answer would be **1**.

## Brute Force Approach

A brute force approach to this problem would involve comparing every interval with every other interval to identify overlaps and then removing intervals accordingly. This would typically involve nested loops, resulting in **O(n^2)** time complexity. Specifically, we'd iterate over each interval, compare it with all others to find overlaps, and count how many intervals need to be removed to eliminate all overlaps.

While this approach works for smaller input sizes, it becomes inefficient as the number of intervals increases, due to the quadratic time complexity.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, think about sorting the intervals in a specific way that allows us to make optimal decisions about which intervals to keep and which to remove. Sorting can help in systematically processing intervals while reducing overlap as much as possible.

## Efficient Solution

The given solution follows a **greedy algorithm** approach, which is much more efficient than the brute force method. Let's break down the code provided:

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time
        intervals.sort()
        
        # Initialize the previous interval end time and count
        prev_end = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap detected, increment the count
                count += 1
                # Keep the interval with the smaller end to minimize future overlaps
                prev_end = min(prev_end, intervals[i][1])
            else:
                # No overlap, update the prev_end to current interval's end
                prev_end = intervals[i][1]
        
        return count
```

**Step-by-Step Explanation**

1. **Sorting the Intervals**: First, we sort the intervals based on their start times. Sorting helps us to process intervals sequentially.
    
2. **Tracking the End of Previous Interval**: We initialize `prev_end` with the end time of the first interval and set a counter `count` to track the number of overlaps that we need to remove.
    
3. **Iterating Over the Intervals**: Starting from the second interval, we check if the current interval overlaps with the previous one:
    
    * If there is an overlap (`intervals[i][0] < prev_end`), we increment the `count` and update `prev_end` to the minimum of the current and previous interval ends. This ensures that we keep the interval that ends earlier, thereby minimizing future overlaps.
        
    * If there is no overlap, we simply update `prev_end` to the end of the current interval.
        
4. **Return the Count**: Finally, we return the count of intervals that were removed.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n log n)**, where **n** is the number of intervals. This is due to the sorting step. The subsequent iteration through the intervals is **O(n)**, which is dominated by the sorting step.
    
* **Space Complexity**: The space complexity is **O(1)**, as we are not using any extra space that scales with the input size, aside from a few variables for tracking purposes.
    

## Conclusion

The **Non-overlapping Intervals** problem is a classic example of how a greedy algorithm can be used to efficiently solve interval scheduling problems. By sorting the intervals and making optimal choices at each step, we can minimize the number of intervals to remove. This solution is not only more elegant but also significantly more efficient than the brute force approach. Next time you come across an interval problem, consider how sorting and a greedy strategy might help you find the solution more effectively.

README for [Non-overlapping Intervals (Leetcode #435)](https://blog.unwiredlearning.com/non-overlapping-intervals) was compiled from the Unwired Learning Blog.