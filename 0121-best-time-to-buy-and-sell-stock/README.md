# Best Time to Buy and Sell Stock (Leetcode #121)

LeetCode's "121. Best Time to Buy and Sell Stock" is a popular question that challenges you to determine the best profit you can achieve from a series of stock prices, given the constraint that you can only buy and sell once. This question tests your ability to effectively use optimization techniques to minimize costs and maximize profits.

## Understanding the Problem Statement

The problem statement is as follows: You are given an array `prices` where `prices[i]` represents the stock price on day `i`. You need to determine the maximum profit you can achieve by buying and selling the stock once. If no profit is possible, you should return `0`. Note that you cannot sell a stock before buying one.

## Brute Force Approach

A common initial approach to this problem is to use a brute force solution. In this approach, you would iterate over all possible pairs of days to determine which combination of buying and selling yields the highest profit. Essentially, you:

* Iterate through every day `i` and for each day `i`, iterate through the subsequent days `j` to compute `prices[j] - prices[i]`.
    
* Track the maximum profit obtained during these comparisons.
    

The brute force solution has a time complexity of `O(n^2)` because it involves nested loops to compare every possible pair of buy and sell days. While this solution is straightforward, it is inefficient for large input sizes, leading to poor performance.

## Hint to Solve the Problem Efficiently

The key to optimizing the brute force solution lies in finding a way to avoid redundant calculations. Instead of evaluating all pairs, think about tracking the lowest buying price as you traverse the list, while also calculating the profit if you were to sell on the current day. By keeping track of the minimum price seen so far and the maximum profit at each step, you can achieve a linear time solution.

## Efficient Solution

Below is an efficient solution for the problem, based on the code provided:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum buy price is the first price
        buy_price = prices[0]

        # the minimum profit is zero
        profit = 0

        for i in range(1, len(prices)):

            # if the current price is less, update the buy_price
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                # else check if we can get a better profit
                current_profit = prices[i] - buy_price
                profit = max(current_profit, profit)

        return profit
```

This solution works by iterating through the list of prices only once, maintaining two key variables:

1. **buy\_price**: Keeps track of the lowest price seen so far, which represents the ideal day to buy the stock.
    
2. **profit**: Tracks the maximum profit obtained up to the current day.
    

During each iteration, if the current price is lower than `buy_price`, we update `buy_price`. Otherwise, we calculate the profit by subtracting `buy_price` from the current price, and update `profit` if the current profit is greater than the previously recorded maximum.

## Time and Space Complexity

* **Time Complexity**: The efficient solution has a time complexity of `O(n)` because it involves a single pass through the `prices` array of length `n`. Each price is considered exactly once, making this approach much more optimal compared to the brute force solution.
    
* **Space Complexity**: The space complexity is `O(1)` since we are only using a constant amount of extra space (`buy_price` and `profit`) to store interim values. There is no additional space requirement that grows with the input size.
    

## Conclusion

By leveraging an iterative approach that maintains the minimum buying price and maximum profit, you can solve the "Best Time to Buy and Sell Stock" problem in an efficient manner. This solution highlights the importance of tracking optimal subproblems while iterating through an array, which is a common strategy in optimization problems.


README for [Best Time to Buy and Sell Stock (Leetcode #121)](https://blog.unwiredlearning.com/best-time-to-buy-and-sell-stock) was compiled from the Unwired Learning Blog.