# Jump Game (Leetcode #55)

Leetcode's "Jump Game" is a fascinating problem that challenges your understanding of greedy algorithms and array traversal. It's a problem often asked during technical interviews, making it important to grasp both its naive and optimized solutions. In this blog, we'll take a deep dive into understanding the problem, discussing a common brute force solution, and finally exploring a more efficient solution backed by the code provided.

## Understanding the Problem Statement

The "Jump Game" problem presents you with an array of non-negative integers, where each element represents your maximum jump length from that position. Your goal is to determine whether you can reach the last index starting from the first index. For example, given the array `[2, 3, 1, 1, 4]`, you start at index `0` and can jump up to `2` steps. From there, you can continue jumping to eventually reach the last index. However, given an array like `[3, 2, 1, 0, 4]`, you will find yourself unable to make it to the last index.

## Brute Force Approach

One common brute force approach is to explore all possible jump paths recursively. At each index, you attempt to jump to every possible position within the given range, checking if any path leads to the last index. The key idea is to start from index `0` and recursively try all reachable positions until you either reach the last index or exhaust all options.

This brute force solution has significant drawbacks, including exponential time complexity due to the redundant exploration of paths. As you might imagine, this approach quickly becomes impractical for larger arrays, making optimization necessary.

## Hint to Solve the Problem Efficiently

Instead of exhaustively trying every path, consider tracking the farthest index you can reach as you iterate through the array. If, at any point, you reach an index that is beyond your current reach, you can conclude that reaching the end is impossible. This optimization relies on the concept of "greedily" advancing as far as possible at each step.

## Efficient Solution

The efficient solution leverages a greedy algorithm to minimize unnecessary calculations. The code provided uses a variable `maxReach` to keep track of the farthest index that can be reached at any given point. As you iterate through the array, you continuously update `maxReach` to be the maximum of its current value or the farthest index reachable from the current position (`i + nums[i]`). If at any point the current index exceeds `maxReach`, it means you cannot proceed further, and the function returns `False`. Otherwise, if you successfully traverse the array and `maxReach` reaches or exceeds the last index, the function returns `True`.

Here is the code:

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # stores the farthest index we can reach
        maxReach = 0
        
        # Iterate through each index in the array
        for i in range(len(nums)):
            # If the current index is greater than the farthest we can reach,
            # it means we cannot reach this index, hence return False
            if i > maxReach:
                return False
            
            # Update maxReach to be the maximum of its current value
            # and the farthest index we can reach from the current index
            maxReach = max(maxReach, i + nums[i])
        
        # If we have iterated through the array and maxReach is at least the last index,
        # it means we can reach the end, hence return True
        return maxReach >= len(nums) - 1
```

## Time and Space Complexity

The time complexity of this solution is **O(n)**, where `n` is the length of the array. This is because we only iterate through the array once, updating `maxReach` as we go. The space complexity is **O(1)**, as we are using a constant amount of extra space regardless of the input size. This efficient time and space usage make the greedy approach a significant improvement over the brute force method.

## **Conclusion**

The "Jump Game" problem serves as a perfect example of how a brute force solution can be optimized using a greedy strategy to achieve linear time complexity. Understanding this problem helps you build intuition for approaching similar array traversal challenges. By focusing on maximizing reach at each step, you can solve this problem efficiently and handle even the largest inputs with ease.

README for [Jump Game (Leetcode #55)](https://blog.unwiredlearning.com/jump-game) was compiled from the Unwired Learning Blog.