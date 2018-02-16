# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/15/2018

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold 
additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution(object):
    """
    last_idx = m + n - 1
    nums1 大小>= m + n
    从nums1 和nums2 最后开始比较
    可能nums1[0]大于nums2[0], 所以当nums1中原来的老元素都往后移动后，nums2还有
    元素，此时这些元素都比nums1[0]小
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
