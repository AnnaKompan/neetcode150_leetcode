"""
Docstring for best_time_buy_stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return
0.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/best-time-to-buy-and-sell-stock/history
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                curr_prof = prices[i] - cheapest
                if curr_prof > max_prof:
                    max_prof = curr_prof
        return max_prof