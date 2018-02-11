# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/09/2018

"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution(object):
    """
    1 & 1 = 1
    1 & 0 = 0
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        m = 1
        for i in range(0, 32):
            if m & n != 0:
                c += 1
            m = m << 2
        return c

class Solution1(object):
    """
    bin(n) & bin(n-1) 移除最小位上的bin(1) 
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in range(0, 32):
            if n != 0:
                c += 1
                n &= n-1
        return c
