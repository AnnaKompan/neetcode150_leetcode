"""
Docstring for valid_palindrome
A valid palindrome is a string that reads the same backward as forward,
after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Time: O(n)
Space: O(n)

Link: https://neetcode.io/problems/is-palindrome/question?list=neetcode150
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. create empty string
        newStr = ""

        # 2. Loop through each char
        for c in s:
        # 3. If char is alphanumeric, convert to lower-case & add to new string
            if c.isalnum():
                newStr += c.lower()

        # 4. Compare new string with its reversed version at return
        return newStr == newStr[::-1]

"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Initialize two pointers (start, end)
        l, r = 0, len(s) - 1

        # 2. While pointers don't cross
        while l < r:
        # 3. While l is less than r and not alphanumeric, move left p
            while l < r and not self.alphaNum(s[l]):
                l += 1

        # 4. While r is bigger than l and not alphanumeric, move right p
            while r > l and not self.alphaNum(s[r]):
                r -= 1

        # 5. If lower chars don't match, return False
            if s[l].lower() != s[r].lower():
                return False

        # 6. Move both pointers inward
            l, r = l + 1, r - 1

        # 7. If loop finishes w/o mismatch, True
        return True

    # Helper f(x) that returns True, if char is alphanumeric
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))