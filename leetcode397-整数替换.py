#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/19
# project = leetcode397-整数替换
from functools import lru_cache


# 给定一个正整数 n ，你可以做如下操作：

# 如果n是偶数，则用n / 2替换n 。
# 如果n是奇数，则可以用n + 1或n - 1替换n 。
# n变为 1 所需的最小替换次数是多少？

class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)  # 记忆化
        def digui(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return 1 + digui(n / 2)
            else:
                return 1 + min(digui(n + 1), digui(n - 1))

        return digui(n)


S = Solution()
print(S.integerReplacement(15))
