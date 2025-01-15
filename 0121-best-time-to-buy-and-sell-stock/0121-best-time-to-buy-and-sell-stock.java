import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            } else {
                int currentProfit = prices[i] - buyPrice;
                profit = Math.max(profit, currentProfit);
            }
        }

        return profit;
    }
}
