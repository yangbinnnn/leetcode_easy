# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/26/2018

"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = {}
        for num in nums:
            try:
                t.pop(num)
                return True
            except:
                t[num] = None
        return False

class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ns = set(nums)
        if len(ns) == len(nums):
            return False
        return True
