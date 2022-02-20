from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        ans = False
        while i < len(bits):
            if bits[i] == 0:
                ans = True
            else:
                i += 1
                ans = False
            i += 1
        return ans
