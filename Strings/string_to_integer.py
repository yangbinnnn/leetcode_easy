# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/26/2018

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given 
input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral
number, or if no such sequence exists because either str is empty or it contains 
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the 
correct value is out of the range of representable values, INT_MAX (2147483647) 
or INT_MIN (-2147483648) is returned.
"""

class Solution(object):
    """
    int(str_n) = ord(str_n) - ord('0')
    9 >= str_n >= 0

    """
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag = 1
        result = 0
        for i, c in enumerate(str.strip()):
            if i == 0 and c == '-':
                flag = -1
                continue
            if i == 0 and c == '+':
                flag = 1
                continue

            if c >= '0' and c <= '9':
                result = result * 10 + (ord(c) - ord('0'))
            else:
                break

            if result * flag >= 2147483647:
                return 2147483647
            if result * flag <= -2147483648:
                return -2147483648

        return result * flag
