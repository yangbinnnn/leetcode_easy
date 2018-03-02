# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/02/2018

"""
Merge two sorted linked lists and return it as a new list. The new list should be 
made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    思路：
    定义一个空节点做为启动，空节点的next 指向最小的node
    然后遍历两个ListNode，将node.next 指向小值，移动node,l1,l2的指针
    但l1 或l2 为None 时说明没有新的node 可以比较，将node.next 指向
    l1 或l2 剩余未比较的 node
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(None)

        while True:
            if l1 is None:
                node.next = l2
                break
            if l2 is None:
                node.next = l1
                break
                
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next

            node = node.next

        return head.next
