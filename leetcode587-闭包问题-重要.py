#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/23
# project = leetcode587-闭包问题
from typing import List


class Solution:
    # Javis算法 所有的点都在pq向量的一侧，即pq与pr的叉积为正，即q为闭包上的点，将p=q
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross_product(point_1, point_2, point_3):
            return (trees[point_2][0] - trees[point_1][0]) * (trees[point_3][1] - trees[point_1][1]) - \
                   (trees[point_2][1] - trees[point_1][1]) * (trees[point_3][0] - trees[point_1][0])

        len_ = len(trees)
        if len_ < 4:
            return trees
        ans = []
        min_left = 100
        begin = 0  # 开始的节点
        for i, val in enumerate(trees):
            if val[0] < min_left:
                min_left = val[0]
                begin = i
        visit = [False] * len_
        visit[begin] = True
        ans.append(trees[begin])
        while True:
            q = (begin + 1) % len_
            for i in range(len_):
                if cross_product(begin, q, i) < 0:
                    q = i
            # 查找在一条直线上的点
            for i in range(len_):
                if not visit[i] and begin != i and q != i and cross_product(begin, q, i) == 0:
                    ans.append(trees[i])
                    visit[i] = True
            if not visit[q]:
                ans.append(trees[q])
                visit[q] = True
            begin = q
            if trees[begin] == ans[0]:
                break

        return ans


solution = Solution()
print(solution.outerTrees([[0, 2], [1, 1], [2, 2], [2, 4], [4, 2], [3, 3]]))
