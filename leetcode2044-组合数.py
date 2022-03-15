#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/15
# project = leetcode2044
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_ = nums[0]
        self.ans = 0

        def digui(temp, k, max_, index):
            if len(temp) == k:
                temp_ans = nums[temp[0]]
                for i in temp:
                    temp_ans = temp_ans | nums[i]
                if temp_ans == max_:
                    self.ans += 1
                return
            else:
                for i in range(index, len(nums)):
                    temp.append(i)
                    digui(temp, k, max_, i + 1)
                    temp.pop()

        for num in nums:
            max_ = max_ | num
        for k in range(1, len(nums) + 1):
            temp = []
            digui(temp, k, max_, 0)
        return self.ans

    def countMaxOrSubsets_ans(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0

        def dfs(pos: int, orVal: int) -> None:
            if pos == len(nums):
                nonlocal maxOr, cnt
                if orVal > maxOr:
                    maxOr, cnt = orVal, 1
                elif orVal == maxOr:
                    cnt += 1
                return
            dfs(pos + 1, orVal | nums[pos])
            dfs(pos + 1, orVal)

        dfs(0, 0)
        return cnt


solution = Solution()
print(solution.countMaxOrSubsets([3, 2, 1, 5]))
