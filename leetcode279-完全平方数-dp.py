#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/8/22
# project = leetcode279-完全平方数-dp
class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt
        l_list = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
        l = [10000] * (n + 1)
        l[1] = 1
        l[0] = 0
        index = 1
        for i in range(2, n + 1):
            if index < len(l_list) and i >= l_list[index - 1]: index += 1
            for k in range(index):
                l[i] = min(l[i], l[i - l_list[k]] + 1)
        return l[n]
