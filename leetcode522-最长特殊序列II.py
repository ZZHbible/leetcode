#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/27
# project = leetcode522-最长特殊序列II
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: len(s), reverse=True)

        def compare(str1, str2):
            i, j = 0, 0
            if len(str1) == len(str2):
                return str1 == str2
            while i < len(str1) and j < len(str2):
                if str1[i] == str2[j]:
                    i += 1
                j += 1
            return False if i < len(str1) else True

        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i == j: continue
                if len(strs[i])>len(strs[j]):break
                if compare(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1


solution = Solution()
print(solution.findLUSlength(["hello", "hemmllo", "good"]))
