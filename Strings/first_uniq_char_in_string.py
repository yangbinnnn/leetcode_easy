# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/29/2018

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        od = collections.OrderedDict()
        for c in s:
            od[c] += od.get(c, 0) + 1
        for v, cnt in od.iteritems():
            if cnt == 1:
                return s.index(v) 
            idx += 1
        return -1

class Solution1(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        sc = collections.Counter(s)
        for i, c in enumerate(s):
            if sc.get(c, -1) == 1:
                return i
        return -1
