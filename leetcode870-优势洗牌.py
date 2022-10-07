#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/10/8
# project = leetcode870-优势洗牌
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted([(nums2[i], i) for i in range(len(nums2))], key=lambda x: x[0])
        index_j, end_j = 0, len(nums1) - 1
        ans = [-1] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] > sorted_nums2[index_j][0]:
                ans[sorted_nums2[index_j][1]] = nums1[i]
                index_j += 1
            else:
                ans[sorted_nums2[end_j][1]] = nums1[i]
                end_j -= 1
        return ans


solution = Solution()
print(solution.advantageCount([12, 24, 8, 32],
                              [13, 25, 32, 11]))
