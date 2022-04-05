#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/5
# project = leetcode762-二进制中质数个计算置位

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0

        def check(i):
            num = 0
            while i:
                if i & 1:
                    num += 1
                i = i >> 1
            if (665772 >> num) & 1:
                return True
            return False

        for i in range(left, right + 1):
            if check(i):
                ans += 1
        return ans
