#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yangbin
# Date: 2018-02-01

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution(object):
    """
    n最后一步可能为n-1或n-2
    n-1最后一步可能为n-2或n-3
    n=3最后一步可能为2或1,共3步
    n=2最后一步可能为1或0,共2步
    n=1时共1步
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n <= 2 else self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution1(object):
    """
    n最后一步可能为n-1或n-2
    n-1最后一步可能为n-2或n-3
    n=3最后一步可能为2或1,共3步
    n=2最后一步可能为1或0,共2步
    n=1时共1步
    """
    c = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        if n in self.c:
            return self.c[n]
        else:
            s = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.c[n] = s
            return s
