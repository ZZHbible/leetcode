#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/20
# project = leetcode549
from collections import defaultdict


class Solution:
    def findLHS(self, nums) -> int:
        record = defaultdict(int)
        for i in nums:
            record[i] += 1
        ret = 0
        for key, val in record.items():
            if key + 1 in record.keys():
                ret = max(ret, val + record[key + 1])
        return ret


solution = Solution()
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(solution.findLHS(nums))
