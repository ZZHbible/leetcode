from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, mid = pow(2, 31), pow(2, 31)
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False
