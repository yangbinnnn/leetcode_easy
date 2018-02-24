# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/24/2018

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = {}
        for num in nums1:
            nums[num] = nums.get(num, 0) + 1

        ret = []
        for num in nums2:
            cnt = nums.get(num, 0)
            if cnt <= 0:
                continue
            ret.append(num)
            nums[num] = cnt - 1
        return ret

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        a = Counter(nums1)
        b = Counter(nums2)
        c = a & b
        return [v for v in c.elements()]
