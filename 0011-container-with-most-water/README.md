# Container With Most Water (Leetcode #11)

In this blog, we will solve LeetCode's 'Container With Most Water' question. We'll start by explaining the problem, discussing a brute-force approach, giving you a hint, and ultimately providing an efficient solution along with its time and space complexity analysis.

## Understanding the Problem Statement

The problem asks you to find two vertical lines from a given array of heights that together with the x-axis, can contain the maximum amount of water. The heights are represented by an array where each element represents the height of a vertical line. You need to identify the pair of lines that, together with the x-axis, form a container capable of holding the most water.

To illustrate: Imagine the heights as the walls of a container and the x-axis as the base. The goal is to find the largest possible container, i.e., the maximum area enclosed by the container walls. You are given an array of non-negative integers, and the area between any two lines is calculated as the product of the distance between the lines and the minimum height of the two lines.

## Brute Force Approach

The brute-force approach to solve this problem is relatively simple: iterate over all possible pairs of lines, calculate the area for each pair, and keep track of the maximum area.

In Python, the brute-force solution would look like:

```python
# Brute-Force Approach
def max_area_bruteforce(height):
    max_area = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area
```

The nested loop goes through each possible pair of indices and calculates the area, storing the maximum found. However, this approach has a time complexity of **O(n^2)**, which makes it inefficient for large input sizes.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, think about reducing the number of comparisons. Instead of checking every possible pair, consider the impact of the width and height on the area. You can use a two-pointer technique to start from the edges and move towards the middle, always keeping track of the maximum area.

The idea here is that by maximizing the width initially and then trying to find a taller line as you move the pointers, you can keep finding areas that have the potential to be the largest.

## Efficient Solution

Here is the efficient solution using the two-pointer technique:

```python
# Efficient Solution
def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area for the current pair of pointers
        area = min(height[left], height[right]) * (right - left)
        # Update the maximum area if the current area is larger
        max_area = max(max_area, area)

        # Move the pointer with the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

**Explanation**

In this solution, we initialize two pointers: `left` at the beginning of the list and `right` at the end. We calculate the area between the two pointers and update the maximum area if the current area is larger.

The key decision is which pointer to move. To maximize the area, we always move the pointer pointing to the shorter line, hoping to find a taller line in subsequent steps that will increase the area. We continue until the two pointers meet.

This approach drastically reduces the number of computations compared to the brute-force solution.

## Time and Space Complexity

* **Time Complexity**: The efficient solution has a time complexity of **O(n)**, where `n` is the number of elements in the input array. This is because each pointer only moves from one end to the other, leading to a single pass through the array.
    
* **Space Complexity**: The space complexity is **O(1)** since we are using only a fixed amount of extra space, independent of the input size.
    

The two-pointer technique offers a significant improvement over the brute-force approach and efficiently solves the problem in linear time.

## Conclusion

The 'Container With Most Water' problem is a classic example that demonstrates how a seemingly complex problem can be solved efficiently using the two-pointer technique. By strategically moving the pointers and reducing the problem space, we can find the optimal solution in linear time, which is a significant improvement over the brute-force approach. Understanding this technique can help you solve many other problems where maximizing or minimizing a value is involved while considering multiple elements in an array. Always remember, efficient problem-solving is about reducing unnecessary calculations and focusing on the core logic.


README for [Container With Most Water (Leetcode #11)](https://blog.unwiredlearning.com/container-with-most-water) was compiled from the Unwired Learning Blog.