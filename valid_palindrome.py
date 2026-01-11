"""
Docstring for valid_palindrome
A valid palindrome is a string that reads the same backward as forward,
after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Time: O(n)
Space: O(1)

Link: https://neetcode.io/problems/is-palindrome/question?list=neetcode150
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))