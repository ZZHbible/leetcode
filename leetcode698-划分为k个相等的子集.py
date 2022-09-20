#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/9/20
# project = leetcode698-划分为k个相等的子集
from functools import lru_cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum, n = sum(nums), len(nums)
        if _sum % k:
            return False
        per = _sum // k
        nums.sort()
        if nums[-1] > per:
            return False

        @lru_cache(None)  # 记忆化搜索
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (nums[i] + p) % per):
                    return True
            return False

        return dfs((1 << n) - 1, 0)


solution = Solution()
print(solution.canPartitionKSubsets([3, 3, 10, 2, 6, 5, 10, 6, 8, 3, 2, 1, 6, 10, 7, 2]
                                    , 6))
