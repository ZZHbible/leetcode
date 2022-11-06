#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/6
# project = leetcode6231-雇佣K位工人的总代价
import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        if len(costs) <= 2 * candidates:
            return sum(sorted(costs)[:k])
        l, r = candidates - 1, len(costs) - candidates
        left, right = costs[:l + 1], costs[r:]
        heapq.heapify(left)
        heapq.heapify(right)
        for i in range(k):
            if l + 1 < r:
                if right[0] < left[0]:
                    ans += heapq.heappop(right)
                    r -= 1
                    heapq.heappush(right, costs[r])
                else:
                    ans += heapq.heappop(left)
                    l += 1
                    heapq.heappush(left, costs[l])
            else:
                num = left + right
                ans = ans + sum(sorted(num)[:k - i])
                break

        return ans
