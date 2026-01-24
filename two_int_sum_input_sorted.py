"""
Docstring for two_int_sum_input_sorted
Given a sorted array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
The returned indices are not zero-based. That is, the first element has index 1, the second element has index 2, and so on.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if not numbers:
        #     return []
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
