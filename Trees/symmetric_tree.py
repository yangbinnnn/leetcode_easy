# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/06/2018

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not root.left and not root.right:
            return True
        
        left = self._ts(root.left)
        right = self._ts(root.right)
        if len(left) != len(right):
            return False
        
        for l, r in zip(left, right):
            if len(l) != len(r):
                return False
            r.reverse()
            if l != r:
                return False
        
        return True
    
    def _ts(self, node):
        levels = []
        def traversal(root, level):
            try:
                levels[level].append(root.val if root else None)
            except:
                levels.append([root.val if root else None])
            if not root:
                return
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        traversal(node, 0)
        return levels


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._is_mirror(root, root)

    def _is_mirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        return (node1.val == node2.val) and \
               self._is_mirror(node1.left, node2.right) and \
               self._is_mirror(node1.right, node2.left)
