#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/7
# project = leetcode875
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=1e9
        while l<r:
            mid=l+((r-l)>>1)
            print(mid)
            temp_ans=0
            for pile in piles:
                temp_ans+=(pile+mid-1)//mid
            print(temp_ans)
            if temp_ans <= h:
                ans=min(ans,mid)
                r=mid
            else:
                l=mid+1
        return ans

solution=Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))