# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/24/2018

"""

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in 
multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
class Solution(object):
    """
    a -> b -> c -> d
    |ad| = |ab| + |bc| + |cd|
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) in [0, 1]:
            return max_profit
        pre_price = prices[0]
        for price in prices[1:]:
            max_profit += max(price-pre_price, 0)
            pre_price = price
        return max_profit
