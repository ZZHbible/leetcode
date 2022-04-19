#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/19
# project = leetcode821-到某一字符的最短距离-左右遍历-重要
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        len_ = len(s)
        ans_left = [1e4] * len_
        ans_right = [1e4] * len_
        l = -1
        for i in range(len_):
            if s[i] != c and l == -1:
                continue
            if s[i] == c:
                ans_left[i] = 0
                l = i
            else:
                ans_left[i] = i - l
        r = len_
        for i in range(len_ - 1, -1, -1):
            if s[i] != c and r == len_:
                continue
            if s[i] == c:
                ans_right[i] = 0
                r = i
            else:
                ans_right[i] = r - i
        ans = [0] * len_
        for i in range(len_):
            ans[i] = min(ans_left[i], ans_right[i])
        return ans
