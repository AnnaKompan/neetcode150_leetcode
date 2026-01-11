"""
Docstring for reverse_linked_list
Given the head of a singly linked list, reverse the list, and return the reversed list.
Time: O(n)
Space: O(1)
Link: https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev