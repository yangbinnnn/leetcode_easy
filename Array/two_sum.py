# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 01/25/2018

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        neg_target_num = target < 0
        for i, v0 in enumerate(nums):
            if v0 > target and not neg_target_num:
                continue
            neg_num = v0 < 0
            for j, v1 in enumerate(nums[i+1:], i+1):
                if (v1 > target) and (not neg_num) and (not neg_target_num):
                    continue
                if v0 + v1 == target:
                    return [i, j]

class Solution1(object):
    """
    使用一个dict,key保存target差值,value保存idx
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i in range(len(nums)):
            if nums[i] in t:
                return [t[nums[i]], i]
            else:
                t[target-nums[i]] = i
