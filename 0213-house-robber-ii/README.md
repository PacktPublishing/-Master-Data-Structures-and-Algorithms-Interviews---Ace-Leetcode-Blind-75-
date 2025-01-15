# House Robber II (Leetcode 213)

The House Robber II problem (Leetcode 213) presents a variation of the classic House Robber problem, which challenges us to find the maximum amount of money we can rob from houses arranged in a circular neighborhood. Since the first and last houses are adjacent, this creates a unique constraint that prevents robbing both the first and the last house.

## Understanding the Problem Statement

Imagine you are a thief planning to rob houses along a circular street, where each house has a certain amount of money. The constraint is that you cannot rob two directly adjacent houses, and because the street is circular, the first and last houses are also considered adjacent. Your goal is to maximize the total amount you can rob without alerting the police.

For instance, if the houses contain money as `[2, 3, 2]`, you cannot rob the first and last house together. Hence, the maximum amount you can rob is `3`. However, if the houses are `[1, 2, 3, 1]`, the optimal approach would yield `4` by robbing houses `2` and `3`.

## Brute Force Approach

A straightforward brute force approach would involve trying all possible combinations of houses to rob, while adhering to the constraint that no two adjacent houses can be robbed. Since the circular layout adds complexity, we need to account for both the inclusion and exclusion of the first and last houses. We could recursively explore each combination, calculating the total loot each time. However, this approach results in an exponential time complexity due to the sheer number of combinations, making it impractical for larger inputs.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, think about breaking it down into simpler subproblems. Since robbing the first house prevents us from robbing the last one, we can split the problem into two scenarios:

1. Robbing houses from the first to the second-last house.
    
2. Robbing houses from the second to the last house.
    

By solving these two subproblems independently and taking the maximum result, we can effectively handle the circular constraint.

## Efficient Solution

The provided solution leverages dynamic programming to solve the problem efficiently by considering the two scenarios outlined above.

Here is the core of the solution:

1. **Base Cases**: If the input list is empty, return `0`. If it contains only one house, return the value of that house.
    
2. **Split the Problem**: Create two lists: one excluding the last house (`skip_last_house`) and one excluding the first house (`skip_first_house`).
    
3. **Helper Function for Robbery**: Use a helper function (`rob_helper`) to solve the linear version of the house robbery problem for both lists. The helper function applies a dynamic programming approach to calculate the maximum amount that can be robbed without alerting the police.
    
4. **Return the Maximum**: The final answer is the maximum value obtained from the two scenarios.
    

Here is the implementation:

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0            
        if len(nums) == 1:
            return nums[0]

        # Create 2 new lists
        skip_last_house = nums[:-1]
        skip_first_house = nums[1:]

        # Get the loot from both possibilities
        loot_skipping_last = self.rob_helper(skip_last_house)
        loot_skipping_first = self.rob_helper(skip_first_house)

        # Return the maximum of 2 loots
        return max(loot_skipping_last, loot_skipping_first)

    def rob_helper(self, nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
```

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(n)`, where `n` is the number of houses. This is because we iterate through the list of houses twice (once for each scenario).
    
* **Space Complexity**: The space complexity is also `O(n)` due to the use of an auxiliary `dp` array to store intermediate results. However, this could be optimized to `O(1)` by keeping track of only the last two values, which would further reduce the memory usage.
    

## Conclusion

The House Robber II problem is a classic example of how dynamic programming can be used to solve optimization problems with constraints. By breaking the circular dependency into two separate scenarios, we simplify the problem into a linear one that can be effectively managed using a helper function. This approach not only ensures optimal performance but also maintains clarity in handling complex conditions like circular arrangements. By leveraging dynamic programming, we achieve a solution that balances both time and space efficiency, making it suitable for large inputs.


README for [palindromic-substrings](https://leetcode.com/problems/palindromic-substrings) was compiled from the Unwired Learning Blog.