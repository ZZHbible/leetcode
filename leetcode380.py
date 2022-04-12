#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/13
# project = leetcode380
import random


class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        l = list(self.s)
        r = random.randint(0, len(l) - 1)
        return l[r]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
obj.insert(2)
obj.insert(3)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
print(param_3)
