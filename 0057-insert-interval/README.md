# Insert Interval (Leetcode #57)

The 'Insert Interval' problem is a common interview question that challenges your understanding of arrays and interval management. In this blog post, we'll take a closer look at how to efficiently solve the problem, breaking down both the naive and optimized approaches. By the end of this guide, you'll have a deeper understanding of how to merge overlapping intervals and insert new intervals into a sorted list.

## Understanding the Problem Statement

The problem, Leetcode 57: Insert Interval, gives you a list of non-overlapping intervals sorted by their start times and a new interval that you need to insert into the list. The task is to ensure that the final list is non-overlapping and sorted. The new interval might overlap with some of the existing intervals, and the solution should merge any overlapping ones.

**Example**

Suppose you have the list of intervals `[[1, 3], [6, 9]]` and a new interval `[2, 5]`. After inserting the new interval and merging any overlapping intervals, the output should be `[[1, 5], [6, 9]]`.

## Brute Force Approach

A brute force approach to this problem would involve iterating through the entire list of intervals to find where the new interval should be placed, inserting it, and then scanning the entire list again to merge overlapping intervals. This solution requires multiple passes through the list, leading to increased time complexity. Although this approach may be intuitive, it is far from optimal for larger inputs. Specifically, you would:

1. Insert the new interval in its correct position.
    
2. Iterate through the list and merge any overlapping intervals.
    
3. Return the final merged list.
    

This method involves multiple passes through the list and hence results in **O(n^2)** time complexity in the worst case, which isn't efficient.

## Hint to Solve the Problem Efficiently

The key to optimizing the solution is to divide the intervals into three categories:

1. Intervals that end before the new interval starts (“left”).
    
2. Intervals that overlap with the new interval (“merge”).
    
3. Intervals that start after the new interval ends (“right”).
    

By categorizing intervals this way, you can simplify the merging process to just one pass through the list, leading to a much more efficient solution.

## Efficient Solution

Let’s dive into the efficient solution provided in the code:

```python
class Solution:
    def insert(self, intervals, newInterval) -> List[List[int]]:
        left, right = [], []
        start, end = newInterval

        for i in intervals:
            # i ends before new_interval starts
            if i[1] < start:  
                left.append(i)

            # i starts after new_interval ends
            elif i[0] > end:  
                right.append(i)

            # i overlaps with new_interval
            else:  
                start = min(start, i[0])
                end = max(end, i[1])

        return left + [[start, end]] + right
```

**Explanation**

1. **Initialization**: Create two lists, `left` and `right`, to store intervals that are clearly not overlapping with the new interval. Extract `start` and `end` values from `newInterval`.
    
2. **Iterating Through Intervals**:
    
    * For each interval, check if it ends before `newInterval` starts. If so, add it to `left`.
        
    * If an interval starts after `newInterval` ends, add it to `right`.
        
    * Otherwise, the intervals overlap, and you need to merge them by updating the `start` and `end`.
        
3. **Final Result**: Combine the `left`, the merged interval, and the `right` intervals to get the final output.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where `n` is the number of intervals. The solution requires only one pass through the list, and every interval is processed once.
    
* **Space Complexity**: The space complexity is **O(n)**, as we use additional lists (`left` and `right`) to store intervals, but these lists are just reordering of the original intervals.
    

## Conclusion

The 'Insert Interval' problem is a great example of how breaking a problem into smaller, manageable parts can lead to a more efficient solution. By categorizing the intervals and only merging when necessary, we achieve a linear-time solution that is both simple and effective. The key takeaway here is to avoid multiple passes through the data whenever possible and instead leverage categorization to streamline operations.

Try implementing this efficient solution on your own, and you’ll be better equipped to tackle similar interval-based problems in coding interviews!

README for [Insert Interval (Leetcode #57)](https://blog.unwiredlearning.com/insert-interval) was compiled from the Unwired Learning Blog.