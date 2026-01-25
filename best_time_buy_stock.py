"""
Docstring for best_time_buy_stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return
0.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Initialize cheapest and max profit vars
        cheapest = prices[0]
        max_prof = 0
        # 2. Loop through prices
        for i in range(len(prices)):
        # 3. If find cheaper price, change cheapest
            if prices[i] < cheapest:
                cheapest = prices[i]
        # 4. Else, calculate current profit
            else:
                curr_prof = prices[i] - cheapest
        # 5. If current profit bigger than max profit, change max profit
                if curr_prof > max_prof:
                    max_prof = curr_prof
        return max_prof

"""
Two Pointer Approach
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Initialize left and right pointers (0, 1) and max profit var
        l, r = 0, 1
        maxProfit = 0
        # 2. While right pointer within array of prices
        while r < len(prices):
        # 3. If price to the left is smaller then right, set current profit and maxprofit (max)
            if prices[l] < prices[r]:
                profit =prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
        # 4. Else, left pointer is set to right position
            else:
                l = r
        # 5. Right pointer moves by 1
            r += 1
        # 6. Return max profit
        return maxProfit