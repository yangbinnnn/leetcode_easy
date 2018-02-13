# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/13/2018

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution(object):
    """
    设结果为max_profit, 最高出售点fmax - 最低买入点fmin
    出售点在买入点之后
    需要两个索引，一个指向最低price(low)，一个指向最高price(high)，且high永远在low后面
    类似于最多连续子数组差值
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pass
