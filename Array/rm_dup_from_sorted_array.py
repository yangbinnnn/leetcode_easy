# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/23/2018

"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        v = nums[0]
        c = 1
        for num in nums[1:]:
            if v == num:
                continue
            nums[c] = num  
            c += 1    
            v = num
        return c   
