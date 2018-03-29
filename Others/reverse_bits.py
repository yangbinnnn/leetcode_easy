# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 03/29/2018


# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer


class Solution:
    # @param n, an integer
    # @return an integer
    # 1 & 1 = 1
    # 0 & 1 = 0
    # bin(1<<1) = 0b10
    # bin(1<0) = 0b1
    # bin(1<<1 | 1<0) = 0b11
    def reverseBits(self, n):
        ret = 0
        for _ in range(32):
            ret |= n & 1
            n = n >> 1
            ret = ret << 1
        # ret最多只能向右移动31次,否则会超过32位
        return ret >> 1






