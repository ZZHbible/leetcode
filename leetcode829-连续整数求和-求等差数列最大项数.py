#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/3
# project = leetcode829-连续整数求和-求等差数列最大项数
from math import sqrt


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        for i in range(1, int(sqrt(2 * n + 1)) + 1):
            if i % 2 == 0:
                if n / i - n // i == 0.5:
                    num = n // i
                    lower_num = i // 2 - 1
                    if num - lower_num > 0:
                        ans += 1
            else:
                if n % i == 0:
                    num = n // i
                    lower_num = (i - 1) // 2
                    if num - lower_num > 0:
                        ans += 1
        return ans
