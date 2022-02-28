#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/28
# project = leetcode1601-最多可达成的换楼请求数目-枚举-重要！
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.cnt = 0
        len_ = len(requests)
        dept = [0] * n

        def dfs(i, step):
            flag = True
            for num in dept:
                if num != 0:
                    flag = False
                    break
            if flag:
                if self.cnt < step:
                    self.cnt = step
            if i >= len_:
                return
            dept[requests[i][0]] -= 1
            dept[requests[i][1]] += 1
            dfs(i + 1, step + 1)
            dept[requests[i][1]] -= 1
            dept[requests[i][0]] += 1
            dfs(i + 1, step)

        dfs(0, 0)
        return self.cnt


solution = Solution()
print(solution.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]))
