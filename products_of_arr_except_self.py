"""
Docstring for products_of_arr_except_self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Time: O(n^2)
Space: O(1)
Link: https://neetcode.io/problems/product-of-array-except-self/question?list=neetcode150
"""
from ast import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        res = []
        for i in range(len(nums)):
            dot_prod = 1
            for j in range(len(nums)):
                if i != j:
                    dot_prod*=nums[j]
            res.append(dot_prod)
        return res
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        res = [1] * (len(nums))
        # [1,1,1,1]
        pref = 1
        for i in range(len(nums)):
            res[i] = pref # res = [1, 1, 2, 8]
            pref *= nums[i] # pref = 1 / 2 / 8 / 48
        post = 1
        for i in range(len(nums)-1,-1, -1):
            res[i] *= post # res = [48,24,12,8]
            post *= nums[i] # post = 6 / 24 / 48 / 48
        return res

