# Find Minimum in Rotated Sorted Array (Leetcode #153)

In this blog, we will explore how to solve the problem of finding the minimum element in a rotated sorted array. This is a common interview question that tests your understanding of array manipulations and efficient search algorithms. We will start by explaining the problem, then discuss a brute force approach, provide a hint for an efficient solution, and finally present the optimal approach using binary search.

## Understanding the Problem Statement

The given problem is to find the minimum element in a rotated sorted array. Imagine a sorted array that has been rotated, meaning that some of its elements from the beginning have been moved to the end, without changing their order. For instance, a sorted array like `[1, 2, 3, 4, 5]` could be rotated to become `[4, 5, 1, 2, 3]`. Your goal is to find the minimum element in such an array, and the task must be solved in an efficient manner.

## Brute Force Approach

A simple approach to solve this problem is to iterate through the entire array, comparing each element to find the minimum value. You could start from the first element and keep updating a variable that holds the minimum value as you progress through the array. This approach would look something like this:

1. Initialize `min_val` to the first element of the array.
    
2. Iterate through the array.
    
3. Update `min_val` if the current element is smaller.
    
4. Return `min_val` at the end.
    

While this approach works, it has a time complexity of O(n), where `n` is the length of the array, and it does not utilize the sorted property of the array, which limits its efficiency.

## Hint to Solve the Problem Efficiently

The problem gives a sorted, rotated array, which suggests that it might be more efficient to solve it by leveraging binary search. The key observation here is that in a rotated sorted array, there is always a point where the order is broken, and that is where the smallest element lies. The hint is to use a divide-and-conquer strategy to take advantage of the sorted nature of the array.

## Efficient Solution

To solve this problem efficiently, we can use a binary search approach. The goal is to reduce the problem size in each iteration, eventually zeroing in on the minimum value. Let’s look at the solution provided:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If the middle element is greater than the rightmost element,
            # it indicates that the smallest element is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # At the end of the loop, left will be pointing at the smallest element.
        return nums[left]
```

**Explanation of the Code**

1. **Initial Setup**: We start by defining two pointers, `left` and `right`, which initially point to the first and last elements of the array.
    
2. **Binary Search Loop**: While `left` is less than `right`, we calculate the midpoint, `mid`.
    
3. **Update Pointers**: The crucial check here is comparing `nums[mid]` to `nums[right]`:
    
    * If `nums[mid]` is greater than `nums[right]`, it means the smallest value must be to the right of `mid`, so we set `left = mid + 1`.
        
    * Otherwise, the smallest value is to the left or could be `mid` itself, so we adjust `right = mid`.
        
4. **Final Result**: When `left` meets `right`, they both point to the smallest element, which is returned.
    

This binary search-based approach has a time complexity of O(log n) because the array is divided into halves in each iteration, and the space complexity is O(1), as no additional space is used.

## Time and Space Complexity

* **Time Complexity**: The solution has a time complexity of O(log n). This is because the binary search reduces the problem size by half in each iteration, making it very efficient for large arrays.
    
* **Space Complexity**: The space complexity is O(1), as no additional data structures are used, and all operations are done in constant space.
    

This efficient approach is ideal for solving the problem quickly, especially when working with large datasets.

## Conclusion

In this blog, we discussed how to find the minimum element in a rotated sorted array. We began with a brute force solution and then moved on to an efficient solution using binary search, which significantly reduces the time complexity from O(n) to O(log n). This approach is not only faster but also uses constant space, making it highly suitable for large arrays. Understanding this problem helps improve your skills in array manipulation and binary search, which are key components in many technical interviews.


README for [Find Minimum in Rotated Sorted Array (Leetcode #153)](https://blog.unwiredlearning.com/find-minimum-in-rotated-sorted-array) was compiled from the Unwired Learning Blog.