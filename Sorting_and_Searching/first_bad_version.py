# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/09/2018


"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    """
    python2用xrange返回一个迭代器,否则用range可能会oom
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(1, n+1): 
            if isBadVersion(i):
                return i
        return 0

class Solution1(object):
    """
    二叉树搜索
    (left + right) 可能会溢出
    https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues
    使用 left + (right-left)/2
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while True:
            if left >= right:
                break

            mid = left + (right-left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
