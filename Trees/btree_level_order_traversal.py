# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 01/28/2018


"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = {}
        def traversal(root, level):
            if not root:
                return
            try:
                levels[level].append(root.val)
            except:
                levels[level] = [root.val]
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        traversal(root, 0)
        return levels.values()


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        def traversal(root, level):
            if not root:
                return
            try:
                levels[level].append(root.val)
            except:
                levels.append([root.val])
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        traversal(root, 0)
        return levels
