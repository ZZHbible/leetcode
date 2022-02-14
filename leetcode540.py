#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/14
# project = leetcode540
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
        return nums[left]

    # 由于数组是有序的，因此数组中相同的元素一定相邻。
    # 对于下标 x 左边的下标 y，如果 nums[y] = nums[y + 1] 则 y 一定是偶数
    # 对于下标 x 右边的下标 z，如果 nums[z]=nums[z+1]，则 z 一定是奇数。
    def ans_singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


solution = Solution()
print(solution.singleNonDuplicate([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]))
