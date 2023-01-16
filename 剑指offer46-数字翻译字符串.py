#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/11
# project = 剑指offer46-数字翻译字符串
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10: return 1
        temp = []
        while num:
            temp.append(num % 10)
            num //= 10
        temp.reverse()
        num = temp
        num = list(map(int, num))
        dp = [0] * len(num)
        dp[0] = 1
        dp[1] = 2 if num[0] != 0 and num[0] * 10 + num[1] >= 10 and num[0] * 10 + num[1] < 26 else 1
        for i in range(2, len(num)):
            begin = dp[i - 1]
            if num[i - 1] != 0 and num[i - 1] * 10 + num[i] >= 10 and num[i - 1] * 10 + num[i] < 26:
                begin += dp[i - 2]
            dp[i] = begin
        return dp[-1]
