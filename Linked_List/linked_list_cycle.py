# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/17/2018

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# http://codingfreak.blogspot.com/2012/09/detecting-loop-in-singly-linked-list_22.html
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = tortoise = head
        while True:
            if not hare:
                return False

            hare = hare.next
            if not hare:
                return False

            hare = hare.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True

