"""
Docstring for valid_anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Time: O(n)
Space: O(n)
Link: https://neetcode.io/problems/valid-anagram/history
"""
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT