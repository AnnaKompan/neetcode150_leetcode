"""
Docstring for two_sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Time: O(n)
Space: O(n)
Link: https://neetcode.io/problems/two-sum/history
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            hash[n] = i
        for i, n in enumerate(nums):   
            difference = target - n
            if difference in hash and hash[difference] != i:
                return [i, hash[difference]]
        return []