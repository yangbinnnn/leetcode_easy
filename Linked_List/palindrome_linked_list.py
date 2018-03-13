# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/11/2018

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    1. 利用两个point，找到中间点，一个每次走2步，另一个每次走1步，最终相差一倍
    2. 翻转前半部分
    3. 比较前半部分和后半部分
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None # 用于指向翻转的前半部分
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next # fast go 2 step

            tmp = slow.next
            slow.next = rev
            # rev 一直落后slow 一个位置
            rev = slow 
            slow = tmp
            # slow = slow.next # slow go 1 step

        if fast:
            slow = slow.next # 到达中间偏右的位置

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        # 如果rev 为空，说明所有节点值相同，否则循环提前结束了
        return not rev
