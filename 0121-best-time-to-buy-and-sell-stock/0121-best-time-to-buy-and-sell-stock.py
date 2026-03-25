class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = prices[0]
        curr_profit = 0

        for p in prices:
            if p < curr_min:
                curr_min = p
            #     curr_max = p
            # else:
            #     curr_max = max(curr_max, p)
            curr_profit = max(curr_profit, p-curr_min)

        return curr_profit
