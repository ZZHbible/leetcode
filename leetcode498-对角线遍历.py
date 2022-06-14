#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/14
# project = leetcode498-对角线遍历
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j, m, n = 0, 0, len(mat), len(mat[0])
        flag = True
        ans = []
        while True:
            if i < 0 or i >= m or j < 0 or j >= n:
                if flag:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            while i >= 0 and i < m and j >= 0 and j < n:
                ans.append(mat[i][j])
                if i == m - 1 and j == n - 1:
                    return ans
                if flag:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            if flag:
                i += 1
            else:
                j += 1
            flag = not flag


solution = Solution()
print(solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
