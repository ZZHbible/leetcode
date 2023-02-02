#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/12/17
# project = leetcode1764-kmp
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        def fail(word):
            f = [-1] * len(word)
            i, j = 1, -1
            while i < len(word):
                while j >= 0 and word[i] != word[j + 1]: j = f[j]
                if word[i] == word[j + 1]: j += 1
                f[i] = j
                i += 1
            return f

        i = 0
        for group in groups:
            f = fail(group)
            j = 0
            while i < len(nums) and j < len(group):
                if nums[i] == group[j]:
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = f[j - 1] + 1
            if j < len(group):
                return False

        return True


solution = Solution()
print(solution.canChoose([[2, 1]], [12, 1]))
