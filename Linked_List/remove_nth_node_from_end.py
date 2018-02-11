# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/02/2018


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
    """
    遍历一次,记录每个节点位置
    找到第n个节点，将n-1指向n+1
    注意只有一个节点和删除头节点的情况
    """
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

class Solution1(object):
    """
    使用两个游标, p1和p2
    两个游标相差n个节点, 当p2到达末尾时，p1为next为需要删除的节点
    
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        # p2移动n
        for _ in range(n):
            p2 = p2.next
        # 删除head
        if not p2:
            return p1.next
        # 开始同步一样,直到最后一个节点
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        # p1.next 为倒数第n个
        p1.next = p1.next.next
        return head
