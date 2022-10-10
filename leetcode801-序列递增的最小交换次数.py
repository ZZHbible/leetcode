#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/10/10
# project = leetcode801-序列递增的最小交换次数
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        if nums1[i] > nums1[i-1] and nums2[i]>nums2[i-1] and nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]: 如果index_i 交换, index_i-1 可交换可不交换
        if nums2[1] > nums1[i-1] and nums1[i]>nums2[i-1] : 如果index_i 交换, index_i-1不能交换; 如果index_i 不交换，index_i-1交换
        if nums1[i] > nums1[i-1] and nums2[i]>nums2[i-1] : 如果index_i 交换, index_i-1交换; 如果index_i 不交换，index_i-1不交换

        '''
        dp = [[0, 0] for _ in range(len(nums1))]
        dp[0][1] = 1
        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1] and nums1[i] > nums2[i - 1] and nums2[i] > nums1[
                i - 1]:
                dp[i][0] = min(dp[i - 1][0],dp[i-1][1])
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
            elif nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
            elif nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
        return min(dp[len(nums1) - 1])


solution = Solution()
print(solution.minSwap([0,1,4,6,8],
[1,2,2,7,10]))
