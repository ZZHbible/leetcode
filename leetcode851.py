#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/15
# project = leetcode851
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ret = [-1] * len(quiet)
        richer_dict = defaultdict(list)
        for i, j in richer:
            richer_dict[j].append(i)
        @lru_cache(None)
        def dfs(i):
            if ret[i] != -1:
                return
            ret[i] = i
            for j in richer_dict[i]:
                dfs(j)
                if quiet[ret[j]] < quiet[ret[i]]:
                    ret[i] = ret[j]

        for i in range(len(quiet)):
            dfs(i)
        return ret
        # 会超时
        # for i in range(len(quiet)):
        #     quietest=i
        #     quiet_val=quiet[i]
        #     l_copy=richer_dict[i]
        #     while l_copy:
        #         next_l = list()
        #         for j in range(len(l_copy)):
        #             if quiet[l_copy[j]] < quiet_val:
        #                 quietest=l_copy[j]
        #                 quiet_val=quiet[l_copy[j]]
        #             if l_copy[j] in richer_dict:
        #                 next_l.extend(richer_dict[l_copy[j]])
        #         l_copy=next_l[:]
        #     ret.append(quietest)


solution = Solution()
richer = [[0, 2], [1, 2]]
quiet = [0, 1, 2]
print(solution.loudAndRich(richer, quiet))
