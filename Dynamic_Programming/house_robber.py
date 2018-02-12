# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/12/2018

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
"""

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self._nums = nums
        self._cache = {}
        return self._max_monney(len(nums))

    def _max_monney(self, n):
        if n == 0:
            return 0
        if n == 1:
            return self._nums[0]
        if n == 2:
            return max(self._nums[0], self._nums[1])
        try:
            a = self._cache[n-2]
        except:
            a = self._max_monney(n-2)
            self._cache[n-2] = a
        try:
            b = self._cache[n-1]
        except:
            b = self._max_monney(n-1)
            self._cache[n-1] = b
        v = max(a + self._nums[n-1], b)
        return v
