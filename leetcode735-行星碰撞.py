#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/13
# project = leetcode735-行星碰撞
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and len(st) >= 1 and (aster < 0 and st[-1] > 0):
                if st[-1] < -aster:
                    st.pop()
                else:
                    if st[-1] == -aster:
                        st.pop()
                    alive = False
            if alive:
                st.append(aster)
        return st
