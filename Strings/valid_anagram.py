# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/25/2018

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution(object):
    """
    1. 长度相同
    2. 每个字符出现的次数相同

    对每个字符计数或排序比较两个字符串
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        if len(s) != len(t):
            return False
        return len(Counter(s)-Counter(t)) == 0

    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)
