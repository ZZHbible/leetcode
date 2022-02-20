#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/21
# project = leetcode838-推多米诺
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        status = ['.'] * len(dominoes)
        s = set()
        for i, val in enumerate(dominoes):
            if val == "L" or val == "R":
                s.add((i, val))
        while len(s):
            s1 = set()
            for i in range(len(s)):
                index, val = s.pop()
                if status[index] != '.':
                    continue
                status[index] = val
                if val == "L":
                    if index - 1 >= 0:
                        if (index - 1, "R") not in s1:
                            s1.add((index - 1, "L"))
                        else:
                            s1.discard((index - 1, "R"))
                else:
                    if index + 1 < len(dominoes):
                        if (index + 1, "L") not in s1:
                            s1.add((index + 1, "R"))
                        else:
                            s1.discard((index + 1, "L"))
            s = s1
        return "".join(status)

    def pushDominoes_ans(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)
                time[i] = 0
                force[i].append(f)

        res = ['.'] * n
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ni = i - 1 if f == 'L' else i + 1
                if 0 <= ni < n:
                    t = time[i]
                    if time[ni] == -1:
                        q.append(ni)
                        time[ni] = t + 1
                        force[ni].append(f)
                    elif time[ni] == t + 1:
                        force[ni].append(f)
        return ''.join(res)


solution = Solution()
print(solution.pushDominoes(".L.R...LR..L.."))
