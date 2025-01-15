# 3Sum (Leetcode #15)

The "3Sum" problem is one of the most popular algorithm challenges on Leetcode, often encountered by developers preparing for technical interviews. The goal is to identify unique triplets in an integer array that sum up to zero. While it seems straightforward at first glance, solving it efficiently requires a solid understanding of sorting, searching techniques, and eliminating duplicates. In this blog, we'll explore both the brute force and efficient approaches to solving the "3Sum" problem, and help you gain a deeper understanding of its complexities.

## Understanding the Problem Statement

The Leetcode problem **"15. 3Sum"** is a classic algorithm problem where you are tasked to find unique triplets in an array that add up to zero. Given an integer array `nums`, your job is to find all distinct triplets `[nums[i], nums[j], nums[k]]` such that they add up to zero, and all indices `i`, `j`, `k` are distinct.

For instance, given the array `nums = [-1, 0, 1, 2, -1, -4]`, the solution would be `[[ -1, -1, 2], [-1, 0, 1]]`. Here, the challenge is not only to find the triplets but also to ensure they are unique, meaning no duplicate solutions.

The array may contain both positive and negative integers, and it's your task to use an efficient algorithm to solve this within a reasonable time limit. Let’s dive into how we can achieve this.

## Brute Force Approach

A straightforward approach to solving this problem is to use three nested loops to iterate through all possible combinations of numbers. Essentially, we would pick three elements at different indices and check if they sum to zero. Here is a rough idea of how the brute force solution might look:

1. Iterate through the array, using three nested loops.
    
2. Check each combination and see if the sum equals zero.
    
3. Store the combination if it satisfies the condition and isn’t a duplicate.
    

While simple to understand, this approach suffers from high computational complexity. Specifically, it has a time complexity of **O(N^3)**, making it impractical for large input arrays due to its inefficiency. This method would also require extra handling to ensure no duplicate triplets are included, further complicating things.

## Hint to Solve the Problem Efficiently

Before diving into the efficient solution, here's a hint for optimizing the brute force approach:

* Sort the array first. This allows you to efficiently avoid duplicate triplets and make use of a more strategic searching method.
    
* Consider how you might reduce three nested loops to just two using a two-pointer technique.
    

Sorting and using two pointers can significantly reduce unnecessary computations and help eliminate duplicates with ease.

## Efficient Solution

The efficient approach leverages sorting and the two-pointer technique. Here's how we can solve the problem step-by-step:

1. **Sort the Array**: Begin by sorting the array. This helps in easily skipping over duplicates and using two pointers effectively.
    
2. **Iterate with a Fixed Pointer**: Use a loop to fix one number, then apply a two-pointer approach for the remaining sub-array.
    
3. **Two-Pointer Technique**: For each fixed element, use two pointers to find the remaining two elements that sum to zero. Start with one pointer at the next element (`left`), and the other pointer at the end (`right`) of the array.
    
4. **Check and Adjust Pointers**: If the sum of the three elements is zero, add it to the result. If the sum is less than zero, increment the `left` pointer; if it's greater, decrement the `right` pointer. This helps in narrowing down the search efficiently.
    

Here’s the code that implements this approach (based on your provided code):

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the second number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the third number
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
```

## Time and Space Complexity

The **time complexity** of this efficient solution is **O(N^2)**, where `N` is the number of elements in the array. Here's why:

* Sorting the array takes **O(N log N)**.
    
* After sorting, we iterate through the array, and for each element, we use the two-pointer technique, which takes **O(N)** time.
    
* Therefore, the overall complexity becomes **O(N log N) + O(N^2) ≈ O(N^2)** for large values of `N`.
    

The **space complexity** is **O(1)** (ignoring the space used for output), as we are not using any additional data structures that grow with input size. The solution modifies pointers in-place and only requires extra space for storing the result.

## Conclusion

The "3Sum" problem is a great example of how simple techniques like sorting and the two-pointer approach can drastically improve efficiency compared to a brute force solution. Understanding the problem, trying the brute force approach, and then optimizing is a powerful problem-solving strategy in algorithm challenges.

By mastering these concepts, you can handle not only the "3Sum" problem but also a wide range of other problems that rely on finding combinations or subsets of elements efficiently.


README for [3Sum (Leetcode #15)](https://blog.unwiredlearning.com/3sum) was compiled from the Unwired Learning Blog.