#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/8/22
# project = leetcode2337-移动片段得到字符串

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0
        # start, target = start.strip('_'), target.strip('_')
        while i < len(start) and j < len(target):
            while i < len(start) and start[i] == '_': i += 1
            while j < len(target) and target[j] == '_': j += 1
            if i == len(start) and j == len(target): break
            if j >= len(target) or i >= len(start) or start[i] != target[j]: return False
            i += 1
            j += 1

        L_start, R_start = [], []
        L_target, R_target = [], []
        for i in range(len(start)):
            if start[i] == 'L':
                L_start.append(i)
            if start[i] == 'R':
                R_start.append(i)
            if target[i] == 'L':
                L_target.append(i)
            if target[i] == 'R':
                R_target.append(i)
        if len(L_start) != len(L_target) or len(R_start) != len(R_target): return False
        for i in range(len(L_start)):
            if L_start[i] < L_target[i]:
                return False
        for i in range(len(R_start)):
            if R_start[i] > R_target[i]:
                return False
        return True
