#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/23
# project = leetcode859
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i, j = -1, -1
        for index, val in enumerate(s):
            if s[index] != goal[index]:
                if i == -1:
                    i = index
                elif j == -1:
                    j = index
                else:
                    return False
        if i != -1 and j == -1:
            return False
        if i == -1 and j == -1:
            if len(s) == len(set(list(s))):
                return False
        if s[i] != goal[j] or s[j] != goal[i]:
            return False
        return True
