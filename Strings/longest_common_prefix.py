# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/27/2018

"""
Write a function to find the longest common prefix string amongst an array of strings.

For example:

{“a”,“a”,“b”} should give “” as there is nothing common in all the 3 strings.

{“a”, “a”} should give “a” as a is longest common prefix in all the strings.

{“abca”, “abc”} as abc

{“ac”, “ac”, “a”, “a”} as a.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''

        i = 0
        for _ in range(len(strs[0])):
            com = ''
            for s in strs:
                if i == len(s):
                    return strs[0][:i]

                if com == '':
                    com = s[i]
                
                if com != s[i]:
                    return strs[0][:i]

            i += 1
        return strs[0][:i]
