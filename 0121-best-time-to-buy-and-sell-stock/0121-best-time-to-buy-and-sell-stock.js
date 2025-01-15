function maxProfit(prices) {
    let buyPrice = prices[0];
    let profit = 0;

    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < buyPrice) {
            buyPrice = prices[i];
        } else {
            let currentProfit = prices[i] - buyPrice;
            profit = Math.max(profit, currentProfit);
        }
    }

    return profit;
}
