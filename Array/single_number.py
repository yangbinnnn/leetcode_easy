# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/23/2018

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    """
    使用一个hash_table存放元素，遍历nums，如果发现hash_table中已存在，则删除hash_table中的
    元素，相当于成对抵消，hash_table中剩下的一个为single one
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = None
        return hash_table.keys()[0]

class Solution1(object):
    """
    利用数学恒等公式
    2 * (a + b + c) - (a + a + b + b + c) = c
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

class Solution2(object):
    """
    利用异或运算
    a XOR 0 = a
    a XOR a = 0
    a XOR a XOR b XOR b XOR c = 0 XOR 0 XOR c = 0 XOR c = c
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a ^= num
        return a
