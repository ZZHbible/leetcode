#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/18
# project = leetcode668-乘法表中第k小的数

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            i, j, count = m, 1, 0
            flag = False
            while i > 0 and j <= n:
                while i * j > mid:
                    i -= 1
                if i * j <= mid:
                    if mid == i * j:
                        flag = True
                    count += i
                j += 1
            if count == k and flag:
                return mid
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left


solution = Solution()
print(solution.findKthNumber(21, 36, 623))
