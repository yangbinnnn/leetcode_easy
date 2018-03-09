# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/09/2018

"""
Given an array where elements are sorted in ascending order, convert it to 
a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height 
balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    [n1, n2] ->
        n2
    n1 

    [n1, n2, n3] ->
        n2 
    n1      n3
    
    [n1, n2, n3, n4] -> 
    [y]
        n2
    n1      n4
         n3

    [x]
            n3
        n2     n4
    n1

    1. 如果为奇数，中间数为root
    2. 如果为偶数, 中间左边的数为root，尽可能保持左边最少，因为high >= len(left_nums)
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._build_tree(nums)


    def _build_tree(self, nums):
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self._build_tree(nums[:mid])
        root.right = self._build_tree(nums[mid+1:])
        return root
