# Merge Intervals (Leetcode #56)

The 'Merge Intervals' problem is a classic challenge you may encounter in coding interviews or competitive programming. It requires an understanding of sorting and working with interval data, making it an excellent test of algorithmic thinking. This blog post will help you grasp the concept, explore common solutions, and ultimately solve it efficiently using Python.

## Understanding the Problem Statement

The 'Merge Intervals' problem on LeetCode asks you to merge overlapping intervals from a given list. You are provided with an array of intervals where each interval is represented as a pair of start and end times. The goal is to merge all overlapping intervals and return a list of non-overlapping intervals.

For example, given intervals `[[1, 3], [2, 6], [8, 10], [15, 18]]`, you should return `[[1, 6], [8, 10], [15, 18]]`. The overlapping intervals `[1, 3]` and `[2, 6]` are merged to form `[1, 6]`.

## Brute Force Approach

A brute force approach to solve this problem would involve comparing each interval with every other interval to see if they overlap, and then merging them accordingly. This requires maintaining a status of whether an interval has been merged or not, leading to a large amount of nested looping.

While this approach is conceptually straightforward, its inefficiency becomes apparent when working with large input sizes. The need to compare every interval with every other one results in an `O(n^2)` complexity, which is impractical for larger datasets. Hence, we seek a more efficient solution.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, the key insight is to **sort the intervals** by their start times. By ensuring all intervals are processed in a sorted order, we can reduce the number of comparisons needed, since we only need to consider merging consecutive intervals.

## Efficient Solution

Below is the efficient Python solution from the provided code. Let’s break it down step-by-step to understand the logic:

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by the start time
        intervals.sort()

        # Step 2: Initialize the result array with the first interval
        merged = [intervals[0]]

        # Step 3: Iterate over the intervals and merge when necessary
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged
```

**Step-by-Step Breakdown:**

1. **Sorting the Intervals**: The first step is to sort the given intervals by their starting points. This helps in systematically comparing each interval with the one immediately preceding it.
    
2. **Initializing the Result Array**: We start by initializing a result list (`merged`) with the first interval, assuming it will serve as the foundation for merging other intervals.
    
3. **Iterative Merging**: We iterate through the sorted intervals starting from the second interval. If the start of the current interval is less than or equal to the end of the last interval in `merged`, it means there is an overlap, and we merge the two by updating the end time. Otherwise, we add the current interval to `merged` as a non-overlapping interval.
    

## Time and Space Complexity

* **Time Complexity**: The sorting step takes `O(n log n)`, and the iteration over the intervals takes `O(n)`. Thus, the overall time complexity of this solution is `O(n log n)`.
    
* **Space Complexity**: The space complexity is `O(n)` if we consider the space needed for the merged intervals. However, since no additional data structures apart from the result list are used, the extra space usage is minimal, making it an efficient solution.
    

## Conclusion

The 'Merge Intervals' problem is a great example of how sorting can simplify the problem-solving process. By using sorting and iterating through the list only once, the above solution provides an efficient way to merge overlapping intervals without the heavy overhead of a brute force approach. With a time complexity of `O(n log n)`, this solution is suitable for practical use, even with larger inputs.

I hope this guide has helped you understand the nuances of solving the 'Merge Intervals' problem efficiently. Now it's your turn to implement this solution and try it with different test cases!

README for [Merge Intervals (Leetcode #56)](https://blog.unwiredlearning.com/merge-intervals) was compiled from the Unwired Learning Blog.