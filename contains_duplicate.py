"""
Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Time: O(n)
Space: O(n)
Link: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
"""
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset =  set() 
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

"""
Solution 2 (Brute Force)
Time: O(n^2)
Space: O(1)
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False