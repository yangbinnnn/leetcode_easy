# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/27/2018

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits))) + 1
        return [n for n in str(num)]
