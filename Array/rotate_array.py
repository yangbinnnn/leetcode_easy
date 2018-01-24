# -*- coding: utf-8 -*-
# Author: Yangbin
# Created: 01/24/2018

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

class Solution(object):
    """
    使用一个中间交换变量保存最后一个元素，将所有元素向后移动一位，将交换变量放第一个
    空间复杂度 1
    时间复杂度 n * k
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = len(nums)
        for _ in range(k):
            n = nums[-1]
            l = c
            while True:
                l -= 1
                if l == 0:
                    break
                nums[l] = nums[l-1]
            nums[0] = n

class Solution(object):
    """
    翻转字符串 -> 翻转前k个元素 -> 翻转后n-k个元素
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self._reverse(nums, 0, len(nums) - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, len(nums) - 1)

    def _reverse(nums, start, end):
        while True:
            if start > end:
                break
            t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
            start += 1
            end += 1

class Solution(object):
    """
    cpython list 的len()时间复杂度为1
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
