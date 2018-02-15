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
    max_profit = max(prices[j] - prices[i])
    j > i
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i, p1 in enumerate(prices):
            for j, p2 in enumerate(prices[i+1:]):
                max_profit = max(max_profit, p2 - p1)
        return max_profit


class Solution1(object):
    """
    设结果为max_profit, 最低买入点min_price
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class Solution2(object):
    """
    设结果为max_profit, 最低买入点min_price
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            elif:
                min_price = price
        return max_profit
