"""
Docstring for longest_consecutive_sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_seq = 1
        curr_seq = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    curr_seq += 1
                else:
                    longest_seq = max(curr_seq, longest_seq)
                    curr_seq = 1
        return max(curr_seq, longest_seq)