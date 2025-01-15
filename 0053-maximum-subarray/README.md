# Maximum Subarray (Leetcode #53)

If you've ever encountered an interview question that asked you to find the maximum sum of a contiguous subarray, you were likely facing Leetcode's **Maximum Subarray** problem. It may sound simple, but for many programmers, it's an interesting challenge that requires a good understanding of both brute force and optimized approaches. Let's walk through this problem step by step to understand how to solve it.

## Understanding the Problem Statement

The **Maximum Subarray** problem asks you to determine the contiguous subarray within a one-dimensional array of integers that has the largest sum. Given an array, you need to find the maximum possible sum of any of its contiguous subarrays.

For instance, consider the array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`. The subarray `[4, -1, 2, 1]` has the largest sum, which equals 6. Your goal is to implement a function that returns this maximum sum efficiently.

## Brute Force Approach

One common approach to solving this problem is to use **brute force**. In this approach, you would consider all possible subarrays of the given array, calculate their sums, and keep track of the highest sum encountered.

Here's a quick outline of how the brute force method would work:

* Iterate through every possible starting point of the subarray.
    
* For each starting point, iterate through every possible ending point.
    
* Calculate the sum for each of these subarrays, and track the maximum value.
    

While this approach is easy to understand, it is computationally expensive. Its time complexity is **O(n^2)**, which makes it impractical for large input arrays due to its inefficiency.

## Hint to Solve the Problem Efficiently

To solve this problem more efficiently, think about how you can calculate the sum of subarrays without recalculating overlapping portions multiple times. Instead of keeping track of all subarrays, focus on finding the maximum sum ending at each position. Consider whether extending the previous subarray is beneficial or whether starting fresh with the current element is a better choice.

## Efficient Solution

The efficient solution to this problem is implemented using an algorithm called **Kadane's Algorithm**. The code for the solution can be found below:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the sum of the subarray ending at the current index
        current_sum = nums[0]
        
        # This will store the maximum sum found so far
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update current_sum to be the maximum of:
            # 1. The current element itself (which means starting a new subarray)
            # 2. The current element + current_sum (which means extending the existing subarray)
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update max_sum to be the maximum of max_sum and current_sum
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum found
        return max_sum
```

In Kadane's Algorithm, we maintain two variables: `current_sum` and `max_sum`. `current_sum` keeps track of the sum of the subarray ending at the current index, while `max_sum` holds the maximum sum found so far.

* For each element, we decide whether to start a new subarray or to add the current element to the existing subarray by choosing the maximum between `nums[i]` and `current_sum + nums[i]`.
    
* We then compare `current_sum` with `max_sum` to keep track of the overall maximum value.
    

This dynamic programming approach ensures that we are considering each element only once, allowing for a very efficient solution.

## Time and Space Complexity

The **time complexity** of Kadane's Algorithm is **O(n)**, where `n` is the number of elements in the array. This is because we traverse the array only once, and at each step, we perform a constant amount of work.

The **space complexity** is **O(1)** because we are using only a fixed amount of extra space, regardless of the size of the input array. This makes Kadane's Algorithm both time and space efficient.

## Conclusion

The **Maximum Subarray** problem is an excellent example of the power of dynamic programming. By switching from a brute force approach to Kadane's Algorithm, we reduce the computation time from **O(n^2)** to **O(n)**. This makes our solution suitable even for large arrays. Understanding and applying Kadane's Algorithm is an essential skill for solving maximum subarray problems efficiently.

Happy coding, and may your subarrays always have maximum sums!

README for [Maximum Subarray (Leetcode #53)](https://blog.unwiredlearning.com/maximum-subarray) was compiled from the Unwired Learning Blog.