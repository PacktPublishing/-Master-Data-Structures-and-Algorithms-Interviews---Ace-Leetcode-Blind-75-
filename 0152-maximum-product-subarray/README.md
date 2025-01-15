# Maximum Product Subarray (Leetcode #152)

Finding the maximum product subarray in an array of integers is a classic coding problem that helps in understanding the nuances of dynamic programming and array traversal. In this blog, we'll break down the problem, discuss a brute force solution, and provide an efficient approach to solving the "Maximum Product Subarray" problem, as seen on LeetCode. By the end, you'll have a clear understanding of how to efficiently solve this problem using a given Python code.

## Understanding the Problem Statement

The problem statement for "Maximum Product Subarray" (LeetCode #152) asks us to determine the contiguous subarray (containing at least one number) within a given array `nums` that has the largest product. The array can contain both positive and negative numbers, and may include zeros. This variability adds complexity, since multiplying by a negative number can make a large positive number negative, and multiplying by zero resets the product to zero.

To put it simply, you need to identify a section of the array whose product is the maximum possible value compared to all other subarrays.

## Brute Force Approach

A common brute force solution to solve this problem is to iterate through every possible subarray, compute their product, and then track the maximum product found. Here's a general idea:

1. Iterate through each element in the array as the starting point.
    
2. For each starting point, iterate through subsequent elements to form subarrays.
    
3. Calculate the product of elements in each subarray and update the maximum product if the current product is greater.
    

This approach is easy to understand but has a high time complexity of O(n²), making it inefficient for larger inputs due to nested loops.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, it's essential to consider that the product of negative numbers can lead to a larger positive product if managed carefully. Maintaining both a minimum and a maximum product at each step helps handle negative numbers and zeros effectively. You should track both the prefix and suffix products, as these can help ensure that we don't miss any potential maximum product, even when encountering zeros.

## Efficient Solution

Below, we explain the efficient solution using the provided Python code. This solution involves iterating through the array while maintaining prefix and suffix products, ensuring that the result is updated with the maximum product encountered. Here's the code:

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_product, right_product = 1, 1
        result = nums[0]

        for i in range(n):
            # if any of left or right product become 0, update it to 1
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1

            # prefix product
            left_product *= nums[i]

            # suffix product
            right_product *= nums[n - 1 - i]

            result = max(result, max(left_product, right_product))

        return result
```

**Explanation**:

1. **Initialization**: We initialize `left_product` and `right_product` to 1, and `result` to the first element of the array.
    
2. **Loop Through Array**: We iterate through the array from both ends simultaneously:
    
    * The prefix product (`left_product`) multiplies elements from left to right.
        
    * The suffix product (`right_product`) multiplies elements from right to left.
        
3. **Handling Zeros**: Whenever a product becomes zero, it's reset to 1 to avoid the propagation of zeros, which could nullify subsequent products.
    
4. **Update Result**: The `result` is updated at each step to keep track of the maximum product found so far.
    
5. **Return Result**: After the loop completes, the maximum product is returned.
    

This solution efficiently computes the result in a single pass through the array, leveraging prefix and suffix calculations to capture the maximum product subarray.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is O(n), where `n` is the length of the array. This is because we only iterate through the array once, making it significantly faster than the brute force approach.
    
* **Space Complexity**: The space complexity is O(1), as we only use a few extra variables (`left_product`, `right_product`, and `result`) regardless of the input size.
    

## Conclusion

The "Maximum Product Subarray" problem is an excellent example of how managing multiple state variables (like prefix and suffix products) can help solve a problem efficiently, even in the presence of negative numbers and zeros. While the brute force approach provides a simple solution, the efficient solution we discussed is much more suitable for larger inputs due to its linear time complexity. Understanding and implementing such efficient techniques is crucial for tackling array-related problems in competitive programming and technical interviews.

README for [Maximum Product Subarray (Leetcode #152)](https://blog.unwiredlearning.com/maximum-product-subarray) was compiled from the Unwired Learning Blog.