# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/25/2018

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and 
ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = s.lower()
        c26 = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = filter(lambda c: c in c26, s)
        s1 = list(s)
        s1.reverse()
        rs = "".join(s1)
        return s == rs

class Solution1(object):
    """
    前半部分等于后半部分倒序
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c26 = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = filter(lambda c: c in c26, s.lower())

        if len(s) in [0, 1]:
            return True

        mid = len(s) / 2
        return s[:mid] == s[-mid:][::-1]
