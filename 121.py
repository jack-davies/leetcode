class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0
        max_profit = 0
        this_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[sell]:
                sell = i
                this_profit = prices[sell] - prices[buy]
                if this_profit > max_profit:
                    max_profit = this_profit
            if prices[i] < prices[buy]:
                buy = i
                sell = i
                this_profit = 0

        return max_profit
