#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yangbin

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    题目的意思就是在不知道前一个node的情况下删除自己，
    通常删除一个节点的方法是将前一个节点的指针指向当前节点的下一个节点
    参数为linked list需要删除的节点，由于无法改变前一个节点的指针，所
    以只能先将当前节点的值改为下一个节点，再讲当前节点的指针指向下下个节点
    相当于删除了自己原有的值
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
