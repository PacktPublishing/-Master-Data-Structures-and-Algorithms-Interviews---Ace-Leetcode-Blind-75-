#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int buyPrice = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            } else {
                int currentProfit = prices[i] - buyPrice;
                profit = std::max(profit, currentProfit);
            }
        }

        return profit;
    }
};
