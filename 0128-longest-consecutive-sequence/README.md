# Longest Consecutive Sequence (Leetcode #128)

In this blog, we'll walk through how to solve Leetcode's **128\. Longest Consecutive Sequence** problem. We will begin by explaining the problem, examining a common brute-force approach, providing hints for optimization, and finally delving into an efficient solution. By the end, you should understand the different strategies to solve this problem and why the efficient approach is preferred.

## Understanding the Problem Statement

**Problem Statement:** Given an unsorted array of integers, find the length of the longest consecutive elements sequence. Your solution must run in **O(n)** time complexity.

**Example:**

Input: `nums = [100, 4, 200, 1, 3, 2]`  
Output: `4`  
Explanation: The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore, its length is `4`.

The challenge here lies in efficiently finding the longest sequence of consecutive numbers. The numbers can appear in any order, and the sequence doesn't necessarily need to be contiguous in the input array.

## Brute Force Approach

The brute-force approach to solve this problem is straightforward:

1. Iterate through each element of the array.
    
2. For each element, try to determine the length of the consecutive sequence starting from that element.
    
3. Use a nested loop to find if the next consecutive number exists in the array.
    

This approach involves repeatedly scanning the array to check for consecutive elements, leading to a time complexity of **O(n²)**. Given the problem's requirement for **O(n)** time complexity, this brute-force solution is not efficient enough for larger inputs.

## Hint to Solve the Problem Efficiently

To solve this problem in **O(n)** time, we need to avoid repeatedly scanning the array. Think about utilizing a data structure that allows for **O(1)** lookup times. Specifically, a **set** can be a very helpful tool here.

The idea is to store all elements in a set and then iterate through the array while trying to build the longest sequence possible, but only under certain conditions. This avoids redundant work and helps achieve linear time complexity.

## Efficient Solution

Below is an efficient solution to the problem, which leverages a **set** to achieve the desired **O(n)** complexity.

```
# Efficient Solution for Longest Consecutive Sequence
def longestConsecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)  # Create a set of numbers for O(1) lookups
    longest_streak = 0
    
    for num in num_set:
        # Check if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Increment the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # Update the longest streak found so far
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
```

## **Explanation of the Code**

1. **Create a Set:** First, we convert the list into a set (`num_set`) to enable **O(1)** lookups.
    
2. **Iterate Through the Set:** For each number in the set, check if it is the start of a sequence by verifying that `(num - 1)` is not in the set. This ensures that we only start counting when we have found the beginning of a sequence.
    
3. **Build the Sequence:** Once we identify a sequence's starting point, we use a `while` loop to determine how long the sequence extends by checking if `(current_num + 1)` is in the set.
    
4. **Update Longest Streak:** After finding the length of the current sequence, we update the `longest_streak` if the current sequence is longer.
    

## Time and Space Complexity

**Time Complexity:** The time complexity of this solution is **O(n)**. Creating the set takes **O(n)** time, and iterating through the set also takes **O(n)** time. Each lookup in the set is **O(1)**, and each number is processed at most twice (once for identifying the start of a sequence and once during sequence building).

**Space Complexity:** The space complexity is **O(n)**, as we need extra space to store the elements in a set. This is necessary to achieve the efficient **O(1)** lookups.

## Conclusion

In this blog, we covered how to solve the **Longest Consecutive Sequence** problem using both brute-force and optimized approaches. The brute-force method is inefficient for large datasets, while the efficient solution leverages a set to achieve **O(n)** time complexity. Understanding when and how to use sets for quick lookups is key to optimizing problems involving sequences or unique elements.

We hope this helps you solve similar problems more effectively! Feel free to try implementing the solution and see how it performs on various test cases.


README for [Longest Consecutive Sequence (Leetcode #128)](https://blog.unwiredlearning.com/longest-consecutive-sequence) was compiled from the Unwired Learning Blog.