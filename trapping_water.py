"""
Docstring for trapping_water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150
"""
from ast import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. Initialize l and r pointers, maxL and maxR vars (will track tallest wall) and result var
        l,r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        res = 0
        # 2. Edge case for empty height array
        if not height:
            return 0
        # 3. While l and r pointers don't cross
        while l < r:
        # 4. If maxL is less than maxR, move l pointer to the right, update maxL and add to result
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
        # 5. Else, move r pointer to the left, update maxR and add to result
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
        # 6. Return result
        return res

