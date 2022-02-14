from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1e6
        for i in range(len(nums) - k + 1):
            if nums[i + k - 1] - nums[i] < ans:
                ans = nums[i + k - 1] - nums[i]
        return ans


solution = Solution()
print(solution.minimumDifference([9, 4, 1, 7], 3))
