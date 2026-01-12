"""
Docstring for group_anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Time: O(n k) where n is number of strings and k is max length of a string
Space: O(n k)
Link: https://neetcode.io/problems/group-anagrams/question?list=neetcode150
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return strs
        anagrams = {}
        for w in strs:
            count = [0] * 26
            for char in w:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(w)

        return list(anagrams.values())

"""
Time: O(n k log k) where n is number of strings and k is max length of a string
Space: O(n k)
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return strs
        anagrams_dict = defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))
            anagrams_dict[key].append(w)
        return list(anagrams_dict.values())
