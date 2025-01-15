# Search in Rotated Sorted Array (Leetcode #33)

he problem **"Search in Rotated Sorted Array"** is a common interview question that challenges one's understanding of searching techniques. You are given a sorted array that has been rotated at some pivot, and you need to find the target value within this array. The goal is to do this efficiently in logarithmic time, making binary search a natural fit.

## Understanding the Problem Statement

Searching for a value in a rotated sorted array can be a tricky problem, especially when trying to do it in an efficient manner. This problem is a frequent topic in coding interviews and tests your ability to adapt standard search algorithms to handle a unique situation. In this blog, we will explore different approaches to solve this problem, starting from a straightforward brute force solution and moving to a more optimized approach using binary search.

The given array is sorted but then rotated, meaning that the original sorted order is disrupted. For example, consider the array `[4, 5, 6, 7, 0, 1, 2]`. This array was originally sorted as `[0, 1, 2, 4, 5, 6, 7]` but was then rotated to create the final sequence. Your task is to write a function to determine if a given target number exists in this rotated array and return its index or `-1` if it does not exist.

## Brute Force Approach

A common approach to solve this problem would be to iterate through each element of the array and check if it matches the target value. Essentially, this is a linear search, and the pseudocode might look like this:

```python
for i in range(len(nums)):
    if nums[i] == target:
        return i
```

This solution has a time complexity of **O(N)** where `N` is the number of elements in the array. This can be inefficient, especially for large arrays, since each element must be checked until the target is found.

## Hint to Solve the Problem Efficiently

A more efficient way to solve this problem is to leverage the fact that the given array is **partially sorted**. If you use a binary search, you can achieve logarithmic time complexity by focusing on specific sections of the array that are sorted. Note that at least one half of the array must always be sorted, even after rotation. This property is crucial in finding the target more efficiently.

## Efficient Solution

Here is the solution code provided, which efficiently solves the problem using a modified binary search:

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if the mid element is the target
            if nums[mid] == target:
                return mid

            # If the left half is sorted
            if nums[mid] >= nums[left]:
                # Check if target lies in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # If the right half is sorted
            else:
                # Check if target lies in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

In this approach, the **left** and **right** pointers are initialized to mark the boundaries of the array. The **mid** index is calculated using `left + (right - left) // 2` to avoid overflow. We then perform the following checks:

1. If `nums[mid]` is equal to the target, we have found the target and return `mid`.
    
2. If the left half of the current section (`nums[left]` to `nums[mid]`) is sorted, we check whether the target lies within this range. If it does, we adjust `right` to `mid - 1`; otherwise, we move the `left` pointer to `mid + 1`.
    
3. If the right half is sorted, we perform a similar check for that half.
    

These logical checks allow us to decide in each iteration which half of the array we can safely discard, eventually locating the target in **O(log N)** time.

## Time and Space Complexity

The time complexity of this efficient solution is **O(log N)**, where `N` is the number of elements in the array. This is due to the nature of binary search, where the problem size is divided in half at each step.

The space complexity is **O(1)**, as we do not use any extra space apart from a few variables to track indices. All operations are performed in place, making this approach highly efficient for large datasets.

## Conclusion

The "Search in Rotated Sorted Array" problem is an excellent example of how modifying classic algorithms, like binary search, can yield efficient solutions to more complex variations of common problems. By understanding the properties of rotated arrays and employing binary search, we can solve the problem in logarithmic time, which is much more efficient compared to a brute force linear search. Mastering this technique will not only help in interviews but also improve your problem-solving skills in real-world scenarios involving partially sorted data.


README for [Search in Rotated Sorted Array (Leetcode #33)](https://blog.unwiredlearning.com/search-in-rotated-sorted-array) was compiled from the Unwired Learning Blog.