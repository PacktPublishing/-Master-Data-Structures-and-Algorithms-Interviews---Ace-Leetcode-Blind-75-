# Coin Change (Leetcode 322)

The Coin Change problem is a fundamental question in computer science and is widely used to understand dynamic programming concepts. This blog will guide you through the problem, different approaches to solve it, and explain an efficient solution step by step.

## Understanding the Problem Statement

The **Coin Change** problem is a classic question in dynamic programming. Given an array of different denominations of coins and a target amount, the objective is to determine the minimum number of coins needed to make up that amount. If it is impossible to make the target amount using the given coins, you need to return -1.

For example, suppose you have coins with denominations `[1, 2, 5]` and an amount of `11`. The expected result would be `3`, as the optimal solution is `5 + 5 + 1`.

This problem is common in financial scenarios where you need to determine the fewest number of currency units required to make up a given value.

## Brute Force Approach

In a brute-force solution, the idea is to consider all possible combinations of coins and recursively explore every possible way to form the target amount. In this approach, you check each coin and recursively subtract it from the target amount, until either a valid combination is found or it becomes impossible.

The brute-force approach can be implemented with the following logic:

1. Start with the target amount.
    
2. Try every coin in the list by subtracting its value from the target amount.
    
3. Recur with the remaining amount.
    
4. Return the minimum number of coins used from all possible combinations.
    

This solution becomes extremely inefficient as the target amount and the number of coin denominations increase, leading to an exponential time complexity due to repeated calculations.

## Hint to Solve the Problem Efficiently

Instead of recalculating results repeatedly for the same subproblems, think about how to store and reuse previous results. This concept is key to reducing the computational overhead in dynamic programming. The code provided uses a **bottom-up dynamic programming approach** to solve the problem efficiently.

## Efficient Solution

The provided code uses a **dynamic programming** technique to solve the Coin Change problem in a more efficient way. Here's the approach:

1. **Initialization**: Create an array `dp` of length `amount + 1` where each element represents the minimum number of coins needed to achieve that amount. Initially, set every element to a value greater than the possible number of coins (`amount + 1`), as a way to signify that those amounts are initially unreachable. Set `dp[0] = 0` because zero coins are required to achieve an amount of zero.
    
2. **Iterate through Each Amount**: For each amount `i` from `1` to `amount`, iterate over each coin in the `coins` list.
    
    * If the current coin value is less than or equal to `i`, update `dp[i]` with the minimum value between `dp[i]` and `dp[i - coin] + 1`. This indicates that you are trying to find the optimal way to make up the current amount by adding one more coin to a previously calculated value.
        
3. **Return the Result**: After filling the `dp` array, the final answer will be in `dp[amount]`. If the value is still `amount + 1`, it means that it is impossible to form the amount with the given coins, so return `-1`. Otherwise, return `dp[amount]`.
    

Here is the provided code:

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # No solution exists, return -1.
        if dp[amount] == amount + 1:
            return -1  
        
        return dp[amount]
```

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(amount \* n)**, where `amount` is the target value and `n` is the number of different coin denominations. This is because we iterate over all values from `1` to `amount` and, for each value, we iterate over all the coin denominations.
    
* **Space Complexity**: The space complexity is **O(amount)**. This is due to the use of the `dp` array, which stores the minimum number of coins required for each amount from `0` to `amount`.
    

By using dynamic programming, we eliminate the need for repeated calculations, leading to an optimal solution for large input values. The use of the `dp` array helps in storing previous results and significantly reduces the number of operations needed to compute the answer.

## Conclusion

The Coin Change problem is an excellent example of how dynamic programming can be used to solve problems involving optimization. While the brute force approach can be highly inefficient, using a dynamic programming solution drastically reduces the time complexity by storing and reusing results of overlapping subproblems. This bottom-up approach is both intuitive and effective for solving similar problems, making it a valuable tool in any programmer's toolkit. Understanding this problem can greatly enhance your skills in dynamic programming and problem-solving in general.


README for [Coin Change (Leetcode 322)](https://blog.unwiredlearning.com/coin-change) was compiled from the Unwired Learning Blog.