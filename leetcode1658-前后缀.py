#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/7
# project = leetcode1658-前后缀
import copy
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = copy.deepcopy(nums)
        left.insert(0, 0)
        right = copy.deepcopy(nums)
        right.append(0)
        for i in range(1, len(left)):
            left[i] += left[i - 1]
            right[len(left) - i - 1] += right[len(left) - i]
        left_index, right_index = 0, 0
        begin = left[left_index] + right[right_index]
        ans = 1e6
        while left_index <= right_index and right_index < len(right) and left_index < len(left):
            if begin == x:
                ans = min(ans, left_index + len(left) - right_index - 1)
            if begin > x:
                right_index += 1
            else:
                left_index += 1
            if left_index <= right_index and right_index < len(right) and left_index < len(left):
                begin = left[left_index] + right[right_index]
            else:
                break

        return ans if ans != 1e6 else -1

    def minOperations_ans(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)

        if total < x:
            return -1

        right = 0
        lsum, rsum = 0, total
        ans = n + 1
        for left in range(-1, n - 1):
            if left != -1:
                lsum += nums[left]
            while right < n and lsum + rsum > x:
                rsum -= nums[right]
                right += 1
            if lsum + rsum == x:
                ans = min(ans, (left + 1) + (n - right))

        return -1 if ans > n else ans