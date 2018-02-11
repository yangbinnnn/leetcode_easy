# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 01/27/2018

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num != 0:
                continue
            for j, next_num in enumerate(nums[i+1:], i+1):
                if next_num != 0:
                    nums[i] = next_num
                    nums[j] = 0
                    break

class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        for i in range(len(nums) - pos):
            nums[-i-1] = 0
