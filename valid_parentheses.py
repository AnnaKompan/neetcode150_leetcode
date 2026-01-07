"""
Docstring for valid_parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Time: O(n)
Space: O(n)
Link: https://neetcode.io/problems/valid-parentheses/history
"""
class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        for str in s:
            if str == '{' or str == '(' or str == '[':
                open.append(str)
            else:
                if open == []:
                    return False
                elif str == ']' and open.pop() != '['or \
                str == ')' and open.pop() != '(' or \
                str == '}' and open.pop() != '{':
                    return False
        return open == []