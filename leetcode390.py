#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/1/2
# project = leetcode390-模拟题

class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step, num = 0, 1, n
        flag = True
        while num > 1:
            if flag:
                head += step
            else:
                if num % 2 != 0:
                    head += step
            flag = not flag
            step = step << 1
            num = num >> 1
        return head + 1
