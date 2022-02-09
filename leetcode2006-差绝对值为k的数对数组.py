from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mmap = defaultdict(int)
        ans = 0
        for i in nums:
            ans += mmap[i - k]
            ans += mmap[i + k]
            mmap[i] += 1
        return ans
