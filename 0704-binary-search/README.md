# Binary Search (Leetcode #704)

Binary Search is a fundamental algorithm often used to quickly find an element in a sorted array. This blog will help you understand how to solve the LeetCode problem 704 - 'Binary Search'. We'll go through a brute force approach first, and then look at an efficient solution to achieve optimal results.

## Understanding the Problem Statement

The problem statement asks you to find a target element within a sorted integer array. If the target exists in the array, you need to return its index; otherwise, return -1. The given array is sorted in ascending order, and you need to solve the problem with O(log n) time complexity if possible.

## Brute Force Approach

A common but less efficient way to solve this problem is to use a linear search. In this approach, you iterate through each element in the array until you find the target element:

* Start from the beginning of the array.
    
* Compare each element with the target.
    
* If the element matches the target, return its index.
    
* If you reach the end of the array without finding the target, return -1.
    

The brute force approach works, but it is inefficient for large arrays since its time complexity is O(n), which means it requires traversing each element in the worst case.

## Hint to Solve the Problem Efficiently

Notice that the given array is sorted. When dealing with sorted data, Binary Search is usually the preferred method to significantly reduce the time complexity. This involves repeatedly dividing the search interval in half, focusing on narrowing down the potential positions of the target value.

## Efficient Solution

The provided solution makes use of the Binary Search algorithm to solve the problem in a more optimal way. Let's look at how the code works:

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the pointers for the start and end of the array
        left, right = 0, len(nums) - 1

        # Continue searching while the search space is valid
        while left <= right:
            # Calculate the middle index of the current search space
            # Using left + (right - left) // 2 to avoid integer overflow
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] > target:
                # If the middle element is greater than the target,
                # narrow the search to the left half of the array
                right = mid - 1
            else:
                # If the middle element is less than the target,
                # narrow the search to the right half of the array
                left = mid + 1

        # Target not found in the array, return -1
        return -1
```

**Explanation**

* **Initialization**: Start with two pointers, `left` at the beginning and `right` at the end of the array.
    
* **While Loop**: The loop runs as long as `left` is less than or equal to `right`, indicating there is still a valid range to search.
    
* **Middle Calculation**: Calculate the midpoint using `left + (right - left) // 2` to prevent potential integer overflow. The middle value is checked against the target.
    
* **Adjust Search Space**: If the middle value matches the target, return its index. If the middle value is greater than the target, adjust the `right` pointer to search the left half. Otherwise, adjust the `left` pointer to search the right half.
    
* **Return Statement**: If the loop ends without finding the target, return `-1`.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is O(log n), as the search space is divided by half in each iteration.
    
* **Space Complexity**: The space complexity is O(1) because we are using only constant extra space.
    

This efficient approach, Binary Search, is far superior to the brute force method for larger datasets, making it an ideal solution when working with sorted arrays.

## Conclusion

Binary Search is a powerful technique for quickly finding elements in a sorted array. By leveraging the divide-and-conquer strategy, it significantly reduces the time complexity compared to a linear search, making it ideal for large datasets. Understanding and implementing Binary Search can be a valuable skill when working with sorted data structures, and it serves as a fundamental building block for more advanced algorithms. Always consider using Binary Search when dealing with sorted arrays to achieve optimal efficiency.


README for [Binary Search (Leetcode #704)](https://blog.unwiredlearning.com/binary-search) was compiled from the Unwired Learning Blog.