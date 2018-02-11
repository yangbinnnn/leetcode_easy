# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 01/28/2018

"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([s[-i] for i in range(1, len(s) + 1)])

class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return [::-1]
