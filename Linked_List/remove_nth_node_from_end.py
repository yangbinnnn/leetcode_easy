#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yangbin

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 建立索引
        idxs = {}
        cur = head
        cnt = 0
        while True:
            idxs[cnt] = cur
            cur = cur.next
            cnt += 1
            if not cur:
                break

        if cnt > 1:
            idx = cnt - n
            # 删除head
            if idx == 0:
                return idxs[1]
            # 删除非head
            node = idxs[idx]
            pre_node = idxs[idx-1]
            pre_node.next = node.next
            return head
        # 只有一个node
        else:
            return None
