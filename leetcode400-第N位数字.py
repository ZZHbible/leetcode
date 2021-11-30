#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/30
# project = leetcode400-第N位数字
from math import ceil


class Solution:
    def findNthDigit(self, n: int) -> int:
        dic = [0] + [i * 9 * pow(10, i - 1) for i in range(1, 10)]
        for i in range(1, len(dic)):  # 求前缀和
            dic[i] = dic[i] + dic[i - 1]
        i = 0
        while (n > dic[i]):  # 确认n所在的位置
            i += 1
        num = ceil((n - dic[i - 1]) / i)  # 在第i位数的第几个中
        num = pow(10, i - 1) + num - 1  # 在全部数的第几个中
        index = (n - dic[i - 1]) % i - 1  # 在num数中的下标index
        ret = list(str(num))[index if index >= 0 else index + i]
        return int(ret)
