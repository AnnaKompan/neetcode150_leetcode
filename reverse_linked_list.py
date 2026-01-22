"""
Docstring for reverse_linked_list (Iterative)
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
        if not head:
            return None
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev =  curr
            curr = nxt
        return prev

"""
Docstring for reverse_linked_list (Recursive)
Time: O(n)
Space: O(n)
"""
class Solution:
    # [0, 1, 2, 3]
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next) # [reverseList(1, 2, 3)]
            head.next.next = head
        head.next = None
        return newHead