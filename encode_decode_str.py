"""
Docstring for encode_decode_str
Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Note: The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Time: O(n) where n is the total number of characters in all strings
Space: O(n)
Link: https://neetcode.io/problems/encode-and-decode-strings/question?list=neetcode150
"""
from ast import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

        

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j+1+length
        return result


