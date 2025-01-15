# Missing Number (Leetcode #268)

Leetcode's 268. Missing Number is a common problem faced by software engineers, testing their problem-solving skills and ability to optimize solutions. This blog aims to help you solve the Missing Number problem efficiently, providing insights into both a brute-force and an optimal solution. Whether you're preparing for an interview or just improving your coding skills, this guide will walk you through the concepts in an easy-to-understand way.

## Understanding the Problem Statement

The Missing Number problem asks you to find a missing element from a given list of integers, ranging from 0 to *n*. The list is of length *n* and contains *n* unique numbers, meaning that exactly one number from the complete range of 0 to *n* is missing. Your task is to determine which number is absent.

For example:

* **Input:** nums = \[3, 0, 1\]
    
* **Output:** 2
    

In this case, the numbers range from 0 to 3 (inclusive), and we notice that the number 2 is missing from the input array.

## Brute Force Approach

A common approach to solve this problem is to compare the sum of numbers in the given array to the sum of numbers from 0 to *n*. The sum of the first *n* natural numbers can be found using the formula:

**Sum(0 to n) = n \* (n + 1) / 2**

You can then iterate through the given array to compute the sum of its elements and find the difference between the expected sum and the actual sum. This difference will give you the missing number.

**Steps for Brute Force Approach:**

1. Calculate the expected sum using the formula.
    
2. Calculate the sum of all elements in the given array.
    
3. The difference between the expected sum and the actual sum is the missing number.
    

**Drawbacks:** Although this approach is easy to understand and implement, it requires an additional iteration over the list and an extra arithmetic operation, leading to a time complexity of **O(n)** and a space complexity of **O(1)**.

## Hint to Solve the Problem Efficiently

If you're familiar with bit manipulation, you might already know that XOR can be extremely helpful in solving problems related to pairing elements. The XOR operator allows us to efficiently cancel out matching numbers while keeping the unique number isolated. The provided code takes advantage of this characteristic to find the missing number in a single iteration.

## Efficient Solution

The provided solution makes use of the XOR operation to solve this problem efficiently in just one pass. Let's take a closer look at the code:

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        # XOR all indices and all elements in nums
        for i in range(n):
            xor = xor ^ i ^ nums[i]

        # Finally XOR with n (since the range is from 0 to n)
        xor = xor ^ n

        return xor
```

In this solution, we initialize `xor` as 0 and iterate through the array. During each iteration, we XOR the current index `i` and the element at that index, `nums[i]`, with `xor`. After the loop completes, we also XOR `xor` with `n` (since the complete range is from 0 to *n*). This operation will cancel out all the numbers that appear twice, leaving only the missing number.

**Example Walkthrough:**

* Consider `nums = [3, 0, 1]`. Here, `n` is 3.
    
* During the loop, we XOR as follows:
    
    * `xor = 0 ^ 0 ^ 3 = 3`
        
    * `xor = 3 ^ 1 ^ 0 = 2`
        
    * `xor = 2 ^ 2 ^ 1 = 3`
        
* After the loop, XOR with `n`: `xor = 3 ^ 3 = 2`
    
* The missing number is 2.
    

## Time and Space Complexity

**Time Complexity:**

* The solution runs in **O(n)** time, as it involves a single pass through the array of length *n*. Each XOR operation takes constant time, leading to an efficient linear runtime.
    

**Space Complexity:**

* The space complexity is **O(1)** since no extra data structures are used and only a constant amount of additional memory is required.
    

## Conclusion

The Missing Number problem is an excellent example of how bit manipulation can help simplify and optimize solutions. While the brute-force approach is straightforward, the XOR method offers a more elegant and efficient solution. If you ever face problems where pairs of elements cancel each other out, XOR is a tool worth considering.

Mastering these techniques will help you tackle similar problems in coding interviews and expand your toolbox of efficient coding strategies. Give it a try and see how the XOR approach works in other scenarios!

README for [Missing Number (Leetcode #268)](https://blog.unwiredlearning.com/missing-number) was compiled from the Unwired Learning Blog.