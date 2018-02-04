#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yangbin
# Date: 2018-02-02

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        for an in range(2, len(nums) + 1):
            for idx in range(len(nums)):
                if an > len(nums) - idx:
                    break
                max_sum = max(sum(nums[idx:idx+an]), max_sum)
        return max_sum


class Solution1(object):
    """
    max(nums[:]) >= max(nums[:len(nums)-1])
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max_end = nums[0]
        for num in nums[1:]:
            max_end = max(max_end+num, num)
            max_num = max(max_end, max_num)
        return max_num
