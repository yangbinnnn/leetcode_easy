# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/03/2018

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._valid(root, float('-inf'), float('inf'))

    def _valid(self, node, min_v, max_v):
        if not node:
            return True

        if node.val <= min_v or node.val >= max_v:
            return False

        return self._valid(node.left, min_v, node.val) and self._valid(node.right, node.val, max_v)
