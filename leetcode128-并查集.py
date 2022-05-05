#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/5
# project = leetcode128-并查集
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(p, x):
            if x != p[x]:
                p[x] = find(p, p[x])
            return p[x]

        len_ = len(nums)
        if len_ <= 0:
            return 0
        mp = {}
        p = [i for i in range(len_)]
        cnt = [1 for _ in range(len_)]
        for i, val in enumerate(nums):
            mp[val] = i
        for i in nums:
            if i - 1 in mp:
                sa, sb = find(p, mp[i - 1]), find(p, mp[i])
                if sa != sb:
                    p[sa] = sb
                    cnt[sb] += cnt[sa]
        return max(cnt)
