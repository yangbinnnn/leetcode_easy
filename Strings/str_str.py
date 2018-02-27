# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/27/2018

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = -1
        match = 0

        if len(needle) == 0:
            return 0

        if len(haystack) < len(needle):
            return idx

        i = 0
        while i < len(haystack):
            if match == len(needle):
                break

            if haystack[i] == needle[match]:
                if idx == -1:
                    idx = i
                match += 1
            else:
                if idx != -1:
                    i = idx # 从idx+1处从新匹配
                idx = -1
                match = 0

            i += 1

        # 循环结束后可能没有完全匹配
        return idx if match == len(needle) else -1
