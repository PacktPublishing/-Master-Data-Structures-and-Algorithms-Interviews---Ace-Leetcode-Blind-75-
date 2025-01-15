# Two Sum II - Input Array Is Sorted (Leetcode #167)

The 'Two Sum II - Input Array Is Sorted' problem from LeetCode is an interesting challenge that tests your ability to efficiently solve a problem using pointers. Let's explore the problem, common brute-force methods, and then dive into the efficient solution with the provided code.

## Understanding the Problem Statement

The problem provides you with a sorted array of integers and a target value. Your goal is to find two numbers from this sorted array such that they add up to the given target. You must return the indices of the two numbers, and the solution should use **1-indexed** positions. Importantly, you are guaranteed that there is exactly one solution, and you cannot use the same element twice.

For instance, given the sorted array `[2, 7, 11, 15]` and target `9`, the numbers `2` and `7` add up to `9`. The answer should be `[1, 2]`.

## Brute Force Approach

A naive way to solve this problem is to use a nested loop to iterate over all possible pairs in the array and find the indices whose elements add up to the target. This brute-force approach looks something like this:

```python
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
```

While this solution is easy to implement, it has a **time complexity of O(n^2)**, which is inefficient for larger input arrays. The double loop makes it computationally expensive.

## Hint to Solve the Problem Efficiently

Because the input array is **sorted**, you can use a more efficient approach by taking advantage of the sorted order. The problem can be solved using two pointers, one starting from the left and one from the right of the array. By moving these pointers intelligently, you can efficiently find the required indices.

## Efficient Solution

The provided code uses the two-pointer technique, which allows us to solve the problem in **O(n)** time complexity. Here's the code:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: left at the start, right at the end.
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # Return the 1-indexed positions if the target sum is found.
            if current_sum == target:
                return [left + 1, right + 1]  
            
            # Move the left pointer to the right if the sum is less than the target.
            elif current_sum < target:
                left += 1
            
            # Move the right pointer to the left if the sum is greater than the target.
            elif current_sum > target:
                right -= 1

        return []
```

In this solution:

* **Left and Right Pointers**: The `left` pointer starts at the beginning of the array, and the `right` pointer starts at the end.
    
* **Sum Evaluation**: At each iteration, you calculate the `current_sum` of the elements at the `left` and `right` pointers.
    
    * If `current_sum` equals the target, you've found the answer and return the indices (`left + 1` and `right + 1` to convert to 1-indexed positions).
        
    * If `current_sum` is less than the target, you increment the `left` pointer to increase the sum.
        
    * If `current_sum` is greater than the target, you decrement the `right` pointer to decrease the sum.
        

This approach ensures that each element is visited at most once, resulting in a **time complexity of O(n)**, which is a significant improvement over the brute-force method.

## Time and Space Complexity

* **Time Complexity**: The two-pointer approach has a time complexity of **O(n)** because both pointers traverse the list from opposite ends and meet in the middle. This is much faster compared to the **O(n^2)** complexity of the brute-force solution.
    
* **Space Complexity**: The solution has a **space complexity of O(1)** since we are only using a fixed amount of additional space for the pointers, making this solution both time and space efficient.
    

## Conclusion

The 'Two Sum II - Input Array Is Sorted' problem can be solved with either a brute-force approach or the more efficient two-pointer technique. Using the two-pointer method takes full advantage of the sorted input array and leads to an optimal solution in terms of time and space complexity.


README for [Two Sum II - Input Array Is Sorted (Leetcode #167)](https://blog.unwiredlearning.com/two-sum-ii-input-array-is-sorted) was compiled from the Unwired Learning Blog.