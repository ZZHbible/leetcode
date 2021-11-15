#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/15
# project = leetcode2017

def gridGame(self, grid) -> int:
    '''
        由题意可知，第二个机器人得到的点数为:min(除去相交那列max(第一行从右往左,第二行从左往右))
    '''
    len_grid = len(grid[0])
    for i in range(len_grid):
        if len_grid - i < len_grid:
            grid[0][len_grid - i - 1] = grid[0][len_grid - i - 1] + grid[0][len_grid - i]  # 求上一行的前缀和，从后往前
        if i - 1 >= 0:
            grid[1][i] = grid[1][i] + grid[1][i - 1]  # 求下一行的前缀和，从前往后
    ret = float('inf')
    for i in range(len_grid):
        ret = min(ret, max(grid[0][i + 1] if i + 1 < len_grid else 0, grid[1][i - 1] if i - 1 >= 0 else 0))

    return ret