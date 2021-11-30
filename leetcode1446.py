#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/1
# project = leetcode1446
class Solution:
    def maxPower(self, s: str) -> int:
        max_ = 1
        ret = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                max_ += 1
            else:
                ret = max(ret, max_)
                max_ = 1
        ret = max(ret, max_)
        return ret
