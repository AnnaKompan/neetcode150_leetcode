"""
Docstring for container_w_most_water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/container-with-most-water/question?list=neetcode150
"""
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = min(l,r)
        # width =  r_idx - l_idx
        # max_amount = w*h
        # 1. Initialize 2 pointers and max_amount for final answer
        max_amount = 0
        l, r = 0, len(heights)-1
        # 2. While left and right don't meet
        while l < r:
        # 3. Current admount is idx difference * min of height from both sides
            cur_amount = (r - l)*min(heights[l], heights[r])
        # 4. Update total max with the current max at each iteration
            max_amount = max(cur_amount, max_amount)
        # 5. if heights on the left <= heights on the right, move l pointer 
            if heights[l]<=heights[r]:
                l += 1
        # 6. if heights on the right <= heights on the left, move r pointer 
            else:
                r -= 1
        # 7. Return max water cointainer can hold
        return max_amount