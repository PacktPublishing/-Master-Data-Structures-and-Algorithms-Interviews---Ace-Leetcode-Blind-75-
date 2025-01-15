# Longest Increasing Subsequence (Leetcode #300)

The 'Longest Increasing Subsequence' problem is a common question that appears in coding interviews and technical assessments, particularly on platforms like LeetCode. This problem tests your understanding of dynamic programming and how to efficiently manage sequences within arrays. In this blog, we will walk through the question itself, discuss the brute-force solution, provide hints, and finally introduce an efficient solution along with the time and space complexity. If you're looking to master this problem, keep reading!

## Understanding the Problem Statement

The question asks you to find the length of the **longest increasing subsequence** in an array of integers. A subsequence is derived by deleting zero or more elements without changing the order of the remaining elements. The task is to return the length of the longest subsequence where each element is greater than the one before it.

For example:

```python
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], which has a length of 4.
```

## Brute Force Approach

A simple, brute-force way to solve this problem would involve generating all possible subsequences, checking each one to determine if it's increasing, and then finding the length of the longest among them. However, this approach has an exponential time complexity of **O(2^n)**, since we are looking at all possible combinations of elements. This method is computationally expensive and impractical for larger arrays.

## Hint to Solve the Problem Efficiently

To solve this problem more efficiently, we need a strategy to keep track of previously computed results and use them for future calculations. The solution provided in the code makes use of **dynamic programming (DP)** to store the length of the increasing subsequence ending at each element.

The idea is to use a DP array where each index represents the length of the longest increasing subsequence ending at that position. By leveraging previously computed values, we can efficiently build up the solution in a single pass through the array.

## Efficient Solution

Here is an efficient dynamic programming approach to solve the problem, as given in the attached solution code:

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums))]
        max_length = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_length = max(max_length, dp[i])
        
        return max_length
```

In this solution:

* **Initialization**: We create a **dp** array with the same length as the input array, where each element is initialized to **1**. This is because the minimum length of an increasing subsequence containing just one element is **1**.
    
* **Nested Loop**: We iterate through the array with two loops. For each element at index **i**, we compare it with every previous element at index **j**.
    
* **Updating DP**: If the current element **nums\[i\]** is greater than **nums\[j\]**, it means we can extend the increasing subsequence ending at **j** by including **i**. Thus, **dp\[i\]** is updated as **max(dp\[i\], dp\[j\] + 1)**.
    
* **Result**: The value **max\_length** keeps track of the maximum length of the subsequence encountered so far.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity for this solution is **O(n^2)**, where **n** is the length of the input array. This is due to the nested loop where each element is compared with every previous element.
    
* **Space Complexity**: The space complexity is **O(n)** because we use an additional array of size **n** to store the length of the subsequence ending at each element.
    

## Conclusion

The 'Longest Increasing Subsequence' problem is a classic example where a brute-force solution might seem intuitive at first but is not feasible for larger inputs. Using dynamic programming allows us to significantly optimize the solution and make it practical for real-world applications. Mastering such problems helps in understanding the core concepts of dynamic programming, which is a crucial part of many technical interviews.

Give this problem a try, and remember, practice makes perfect when it comes to mastering dynamic programming techniques!

README for [Longest Increasing Subsequence (Leetcode #300)](https://blog.unwiredlearning.com/longest-increasing-subsequence) was compiled from the Unwired Learning Blog.