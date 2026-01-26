"""
Docstring for 3sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Time: O(n^2)
Space: O(n)
Link: https://neetcode.io/problems/3sum/question?list=neetcode150
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1. Sort numbers to avoid duplicates
        nums.sort()
        # 2. Main loop to find first number and its idx
        for i, a in enumerate(nums):
        # 3. Skip duplicates of first number if i > 0
            if i > 0 and a  == nums[i-1]:
                continue
        # 4. Fins two remaining numbers using l, r pointers (from i and the end)
            l, r = i + 1, len(nums) - 1
        # 5. While l < r, count sum of 3 numbers
            while l < r:
                threeSum = a + nums[l] + nums[r]
        # 6. If 3sum > 0, control it by lowering r pointer
                if threeSum > 0:
                    r -= 1
        # 7. If 3sum < 0, control it by moving l higher
                elif threeSum < 0:
                    l += 1
        # 8. Else, append results to arr, move l pointer
        # 9. While avoid duplicates of l number, and l < r, move l pointer 
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        # 10. Return result arr
        return res
"""
Brute Force Approach
Time: O(n^3)
Space: O(n)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Use set to avoid duplicates
        res = set()
        # 2. Sort arr of nums
        nums.sort()
        # 3. 3 nested loops for each num
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
        # 4. If triple == 0, create temp list and add tuple to res
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        # 5. Return list of lists
        return [list(i) for i in res]