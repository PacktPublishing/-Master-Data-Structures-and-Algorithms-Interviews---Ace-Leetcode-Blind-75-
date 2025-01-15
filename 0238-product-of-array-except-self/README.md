# Product of Array Except Self (Leetcode #238)

Leetcode problem 238, "Product of Array Except Self," is a popular coding problem that helps you enhance your understanding of array manipulation, efficient iteration, and avoiding redundant computations. Let's explore how to solve this problem in various ways, including a brute force approach and an efficient solution.

## Understanding the Problem Statement

You are given an array of integers `nums`, and you need to return an array `output` such that each element at index `i` is the product of all elements in the original array except the element at `i`. The problem comes with some constraints: you cannot use the division operator, and the solution must run in O(n) time complexity while using only constant extra space (excluding the output array).

**Example**

* **Input**: `nums = [1, 2, 3, 4]`
    
* **Output**: `[24, 12, 8, 6]`
    

The output indicates that for each index, we take the product of all elements except the one at the current index.

## Brute Force Approach

A common approach to solve this problem is by using a brute force method. The brute force approach involves iterating through each element and calculating the product of all other elements for that index. To achieve this:

1. Loop through each element in the input array.
    
2. Use a nested loop to calculate the product of all elements except the current element.
    

The code for a brute force approach would look something like this:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result.append(product)
        return result
```

This approach works but has a significant drawback: it results in a time complexity of **O(n^2)** due to the nested loop. This solution is inefficient for large input arrays.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, we need to think about how to calculate the product for each element without repeatedly multiplying all the values every time. The key idea is to calculate products in two passes:

* **Left Product**: Calculate the cumulative product of elements to the left of the current element.
    
* **Right Product**: Calculate the cumulative product of elements to the right of the current element.
    

By combining these two values for each element, we can get the final product for each index without recalculating anything redundantly.

## Efficient Solution

The efficient solution involves using two auxiliary arrays to store the left and right products for each element, followed by combining them to get the result. Here is the code provided, which follows this idea:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Array to store all left multiplication
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Array to store all right multiplication
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Calculate the result array by multiplying left and right products
        result = [1] * n
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
```

**Step-by-Step Explanation**

1. **Left Product Calculation**:
    
    * Create an array `left` where `left[i]` stores the product of all elements to the left of index `i`.
        
    * Initialize `left` as `[1] * n` because there are no elements to the left of the first element.
        
    * Iterate through the array from index 1 to `n-1`, and calculate `left[i]` as `left[i-1] * nums[i-1]`.
        
2. **Right Product Calculation**:
    
    * Create an array `right` where `right[i]` stores the product of all elements to the right of index `i`.
        
    * Initialize `right` as `[1] * n` because there are no elements to the right of the last element.
        
    * Iterate through the array from `n-2` to 0, and calculate `right[i]` as `right[i+1] * nums[i+1]`.
        
3. **Final Result Calculation**:
    
    * Create the `result` array by multiplying the corresponding elements from `left` and `right` arrays.
        
    * Set `result[i] = left[i] * right[i]` for each index `i`.
        

This solution calculates the product for each element in O(n) time, without using nested loops.

## Time and Space Complexity

* **Time Complexity**: The solution runs in **O(n)** time. We make three passes through the input array:
    
    1. One to compute the `left` products.
        
    2. One to compute the `right` products.
        
    3. One to compute the final result array. Each pass takes linear time, making the overall time complexity O(n).
        
* **Space Complexity**: The space complexity is **O(n)** due to the additional `left` and `right` arrays. However, the problem can be solved in **O(1)** extra space if we use the output array to store intermediate results (excluding the output array itself).
    

## Conclusion

The key to solving "Product of Array Except Self" efficiently is to recognize how you can precompute parts of the result (i.e., left and right products) and combine them in a meaningful way. This approach avoids using division, handles all elements in linear time, and minimizes redundant calculations. It's a perfect example of leveraging precomputation to solve complex problems elegantly and efficiently.


README for [Product of Array Except Self (Leetcode #238)](https://blog.unwiredlearning.com/product-of-array-except-self) was compiled from the Unwired Learning Blog.