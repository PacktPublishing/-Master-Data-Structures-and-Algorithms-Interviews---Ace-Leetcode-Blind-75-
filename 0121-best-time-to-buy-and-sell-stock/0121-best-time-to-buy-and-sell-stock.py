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
    

#Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#Blog: https://blog.unwiredlearning.com/best-time-to-buy-and-sell-stock