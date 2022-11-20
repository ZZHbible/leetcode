#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/20
# project = leetcode6243-到达首都的最少油耗
import math
from collections import defaultdict
from typing import List


class Solution:
    '''
        用hash表存图信息
        从外围往内算度为1的节点，将所有在外围节点的num加入与之连接的节点
    '''
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        mmap = defaultdict(list)
        ans = 0
        num_mmap = [1] * (len(roads) + 1)
        for road in roads:
            begin, end = road
            mmap[begin].append(end)
            mmap[end].append(begin)
        del_key = []
        for key, val in mmap.items():
            if key == 0: continue
            if len(val) == 1:
                del_key.append(key)

        while len(mmap) > 1:
            copy_del_key = []
            for key in del_key:
                ans += math.ceil(num_mmap[key] / seats)
                for i in mmap[key]:
                    num_mmap[i] += num_mmap[key]
                num_mmap[key] = 0
                mmap[mmap[key][0]].remove(key)
                if len(mmap[mmap[key][0]]) == 1 and mmap[key][0]:
                    copy_del_key.append(mmap[key][0])
                del mmap[key]
            del_key = copy_del_key
        return ans
