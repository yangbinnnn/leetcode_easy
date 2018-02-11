# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 02/07/2018


"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        c = 0
        for i in range(2, n):
            if self._is_prime(i):
                c += 1
        return c

    def _is_prime(self, num):
        for i in xrange(2, num-1):
            if num % i == 0:
                return False
        return True

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        not_primes = [False] * n
        c = 0
        for i in xrange(2, n):
            if not not_primes[i]: 
                c += 1
                for j in xrange(2, n):
                    if i * j >= n:
                        break
                    not_primes[i*j] = True
        return c
