"""
Docstring for top_k_frequent_element
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Time: O(n log n) where n is number of elements in the array
Space: O(n)
Link: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
"""
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return sorted(counter, key= lambda x: counter[x], reverse=True)[:k]
"""
Time: O(k log n) where n is number of elements in the array, k is number of top frequent elements to return
Space: O(n)
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))

        result=[]
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result
        