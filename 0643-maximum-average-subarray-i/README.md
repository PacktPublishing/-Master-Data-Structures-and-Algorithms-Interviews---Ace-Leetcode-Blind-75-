# Maximum Average Subarray I (Leetcode #643)

Finding maximum average subarrays is a common problem that tests your understanding of sliding window techniques, which are essential for optimizing array operations. In Leetcode problem #643, we need to determine the maximum average of a subarray of length `k`. This challenge not only involves calculating averages efficiently but also learning how to manage subarray calculations without unnecessary redundancies. Let's break down the problem, understand the brute-force solution, and then delve into a more efficient approach.

## Understanding the Problem Statement

The goal of Leetcode problem #643, **Maximum Average Subarray I**, is to find the maximum average of any subarray of length `k` within a given list of integers `nums`. For instance, if you have an input array `nums = [1, 12, -5, -6, 50, 3]` and `k = 4`, the objective is to determine which subarray of size `k` yields the highest average value.

Key constraints include `1 <= k <= nums.length <= 10^5` and `-10^4 <= nums[i] <= 10^4`, which means the input can contain up to 100,000 elements. This makes an efficient solution critical due to the potentially large size of the array.

## Brute Force Approach

The brute-force method for solving this problem involves calculating the sum of each possible subarray of length `k` and then dividing by `k` to obtain the average. You would then track the highest average found among all subarrays. This can be accomplished through the following steps:

1. Initialize a variable to store the maximum average found so far.
    
2. Iterate through all possible starting points for subarrays of size `k`.
    
3. For each subarray, calculate the sum and then divide it by `k` to find the average.
    
4. Compare this average with the current maximum average and update if necessary.
    

While easy to understand, this brute-force approach is inefficient for large inputs due to its time complexity of `O(n * k)`, where `n` is the length of the array. Repeatedly recalculating the sum of overlapping subarrays results in many redundant operations.

## Hint to Solve the Problem Efficiently

Instead of recalculating the sum of each subarray from scratch, think about whether there's a way to avoid redundant computations when transitioning from one subarray to the next. Notice that each subarray overlaps with the previous one, and each sliding window operation only involves removing one element and adding a new one. This observation hints towards the **Sliding Window** technique, which can help you significantly reduce the number of operations required.

## Efficient Solution

To solve this problem more efficiently, we can use the **Sliding Window** approach to maintain a running sum of the current subarray of length `k`. As we slide the window across the array, we adjust the sum by subtracting the element that is left behind and adding the new element. This method avoids recalculating the sum from scratch for each subarray, resulting in a time complexity of `O(n)`, where `n` is the length of the array.

Here is the efficient solution provided:

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sum for starting window
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum
        
        # Start sliding window
        start_index = 0
        end_index = k
        
        while end_index < len(nums):
            # Remove previous element
            current_sum -= nums[start_index]  
            start_index += 1
            
            # Add next element
            current_sum += nums[end_index]  
            end_index += 1
            
            # Update max sum
            max_sum = max(max_sum, current_sum)  
        
        # Return the average
        return max_sum / k
```

In the above code:

1. We first initialize `current_sum` by summing up the first `k` elements of the array.
    
2. We then use two pointers (`start_index` and `end_index`) to manage the window of length `k` as it slides from left to right across the array.
    
3. In each iteration, we update `current_sum` by subtracting the element at `start_index` and adding the element at `end_index`, effectively moving the window one position forward.
    
4. The maximum sum is updated whenever a new higher sum is found.
    
5. Finally, we return the average by dividing `max_sum` by `k`.
    

## Time and Space Complexity

**Time Complexity**: The time complexity of this solution is `O(n)`, where `n` is the length of the input array. This is because we iterate through the entire array once, and each update operation (adding and subtracting elements from `current_sum`) takes constant time.

**Space Complexity**: The space complexity is `O(1)` since the solution only uses a fixed amount of extra space (variables like `current_sum`, `max_sum`, etc.), regardless of the size of the input array.

By avoiding redundant computations and efficiently sliding the window across the array, this solution dramatically improves performance compared to the brute-force approach, making it feasible to handle large inputs as required by the problem constraints.

## Conclusion

The **Maximum Average Subarray I** problem is a great example of how optimizing calculations through efficient techniques like the sliding window can significantly improve performance. By avoiding redundant computations, we reduce the time complexity from `O(n * k)` in the brute-force approach to `O(n)`. This approach allows us to handle even large inputs effectively, making it an important technique for solving similar array-based problems. Understanding and applying the sliding window technique is crucial for optimizing many real-world applications where efficiency is key.


README for [Maximum Average Subarray I (Leetcode #643)](https://blog.unwiredlearning.com/maximum-average-subarray-i) was compiled from the Unwired Learning Blog.