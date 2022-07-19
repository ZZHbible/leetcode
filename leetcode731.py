#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/19
# project = leetcode731
from collections import defaultdict


class MyCalendarTwo:

    def __init__(self):
        self.mmap = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.mmap[start] = self.mmap.get(start,0) + 1
        self.mmap[end] = self.mmap.get(end,0) - 1
        cnt = 0
        for key in sorted(self.mmap):
            cnt+=self.mmap[key]
            if cnt > 2:
                self.mmap[start] = self.mmap.get(start,0) - 1
                self.mmap[end] = self.mmap.get(end,0) + 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start, end)
