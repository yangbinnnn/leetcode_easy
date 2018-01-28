# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/28/2018

"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        x = x if not neg else -x
        r = 0
        m = 2**31
        while True:
            if r >= m:
                return 0
            if x == 0:
                break
            tail = x % 10
            n = r * 10 + tail
            if ((n - tail) / 10) != r:
                return 0
            r = n
            x /= 10
        return r if not neg else -r
