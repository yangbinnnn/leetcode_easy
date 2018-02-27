# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/27/2018

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

设第n个序列为f(n), 则
f(n) = f(f(n-1))
f(n-1) = f(f(n-2))
...
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        s = pre = ''
        cnt = 0
        for i in self.countAndSay(n-1):
            if not pre:
                pre = i
            if pre == i:
                cnt += 1
            else:
                s += '%s%s' % (cnt, pre)
                pre = i
                cnt = 1
        if cnt:
            s += '%s%s' % (cnt, pre)
        return s
