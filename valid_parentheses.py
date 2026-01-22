"""
Docstring for valid_parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Time: O(n)
Space: O(n)
Link: https://neetcode.io/problems/validate-parentheses/question?list=neetcode150
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']':'[', '}':'{', ')':'('}
        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False