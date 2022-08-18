from typing import List
from collections import defaultdict


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count, feq = defaultdict(int), defaultdict(int)
        ans, maxFeq = 0, 0
        for i, num in enumerate(nums):
            if count[num]:
                feq[count[num]] -= 1
            count[num] += 1
            maxFeq = max(maxFeq, count[num])
            feq[count[num]] += 1
            if maxFeq == 1 or maxFeq - 1 == i or feq[maxFeq] == 1 and feq[maxFeq - 1] == (i + 1 - maxFeq) / (
                    maxFeq - 1) or feq[maxFeq] == i / maxFeq and feq[1] == 1:
                ans = max(ans, i + 1)
        return ans


solution = Solution()
print(solution.maxEqualFreq(
    [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 42, 21, 45, 27, 78, 39, 78, 24, 47, 60, 22,
     33, 45, 18, 56, 91, 93, 66, 79, 65, 43, 7, 57, 63, 74, 25, 11, 14, 100, 95, 19, 3, 22, 18, 94, 52, 91, 33, 95, 16,
     93, 63, 65, 8, 88, 51, 47, 7, 51, 77, 36, 48, 89, 72, 81, 75, 13, 69, 9, 31, 16, 38, 34, 76, 7, 82, 10, 90, 64, 28,
     22, 99, 40, 88, 27, 94, 85, 43, 75, 95, 86, 82, 46, 9, 74, 67, 51, 93, 97, 35, 2, 49]))
