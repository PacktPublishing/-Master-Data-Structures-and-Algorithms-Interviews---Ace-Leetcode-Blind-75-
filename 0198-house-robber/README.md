# House Robber (Leetcode 198)

The House Robber problem is a classic example of a dynamic programming challenge that is commonly featured in coding interviews. It requires you to maximize your earnings from robbing houses while adhering to specific constraints that prevent robbing two adjacent houses. In this blog, we'll walk through a brute force solution, provide hints, and present an efficient dynamic programming approach to solve the problem.

## Understanding the Problem Statement

The **House Robber** problem is a popular interview question that helps assess one's ability to solve dynamic programming challenges. The problem is simple to describe: Given an array of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob without robbing two adjacent houses.

To illustrate, imagine a neighborhood where each house has a specific amount of cash. If you rob any house, you cannot rob the adjacent house. The task is to determine how to maximize your earnings while following this constraint. For example:

Input: `nums = [2, 7, 9, 3, 1]`  
Output: `12`  
Explanation: Rob house 1 (cash = 2), skip house 2, rob house 3 (cash = 9), and rob house 5 (cash = 1). Total = 2 + 9 + 1 = 12.

## Brute Force Approach

The simplest way to solve this problem is using a **recursive approach**, trying to consider all possible combinations of robbing houses. For each house, you either rob it and move to the house after the next one or skip it and move to the next house. This approach involves checking every possible combination, leading to exponential time complexity. Here's a basic version of this approach:

* Define a recursive function that takes the current index of the house.
    
* For each house, you have two options: rob it or skip it.
    
* Calculate the maximum sum for each possibility and return the larger value.
    

While this approach is easy to understand, it is not efficient. Its time complexity is **O(2^n)**, as it branches out with each decision, leading to a lot of redundant calculations.

## Hint to Solve the Problem Efficiently

The provided code hints at using a **dynamic programming** approach to eliminate redundant calculations. The idea is to use a table to store the maximum amount that can be robbed up to each house, thus avoiding recalculating the same subproblems.

## Efficient Solution

The optimal solution for the **House Robber** problem involves using **dynamic programming** to track the maximum amount of money that can be robbed up to each house without alerting the police. Let’s walk through the solution provided in the code:

1. **Edge Cases**: If the list is empty, return `0`, since there are no houses to rob. If there is only one house, the answer is simply the value in that house.
    
2. **Dynamic Programming Table Setup**: Create a `dp` array where `dp[i]` represents the maximum amount of money that can be robbed up to house `i`.
    
    * Initialize `dp[0]` to `nums[0]` (the first house).
        
    * Initialize `dp[1]` to the maximum of `nums[0]` and `nums[1]`, as you can only rob one of the first two houses.
        
3. **Filling the DP Table**: Use a loop to fill in the `dp` table for all remaining houses:
    
    * For each house `i` from index `2` onward, decide whether to rob house `i` (and add it to `dp[i-2]`) or skip it and take the value of `dp[i-1]`.
        
    * `dp[i] = max(dp[i-2] + nums[i], dp[i-1])`
        
4. **Result**: Finally, the maximum money that can be robbed is stored in `dp[-1]`.
    

Here’s the code:

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]
```

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where `n` is the number of houses. This is because we iterate through the list of houses once, calculating the maximum possible sum for each house.
    
* **Space Complexity**: The space complexity is **O(n)** due to the `dp` array used to store the maximum amount robbed up to each house. However, this can be further optimized to **O(1)** by only keeping track of the last two values instead of maintaining the entire `dp` array.
    

## Conclusion

The House Robber problem is a great exercise in understanding how dynamic programming can simplify complex problems by breaking them down into subproblems and storing intermediate results. By using dynamic programming, we avoid redundant calculations, thereby significantly improving efficiency. This approach makes it possible to solve the problem in linear time, making it suitable for larger inputs and real-world scenarios.


README for [House Robber (Leetcode 198)](https://blog.unwiredlearning.com/house-robber) was compiled from the Unwired Learning Blog.