#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/16
# project = leetcode432-全O(1)的数据结构
class AllOne:

    def __init__(self):
        self.strdict = {}
        self.max_str = ""
        self.min_str = ""
        self.max_count = 0
        self.min_count = 5e4

    def inc(self, key: str) -> None:
        if key in self.strdict:
            self.strdict[key] += 1
        else:
            self.strdict[key] = 1
        if self.max_str != "":
            if self.strdict[key] > self.strdict[self.max_str]:
                self.max_count = self.strdict[key]
                self.max_str = key
        else:
            self.max_str = key
            self.max_count = self.strdict[self.max_str]

        if self.min_str != "":
            if key == self.min_str:
                self.min_count = 5e4
                self.min_str = ""
                for key, val in self.strdict.items():
                    if val < self.min_count:
                        self.min_str = key
                        self.min_count = val
            if self.strdict[key] < self.strdict[self.min_str]:
                self.min_count = self.strdict[key]
                self.min_str = key
        else:
            self.min_count = self.max_count
            self.min_str = self.max_str

    def dec(self, key: str) -> None:
        if self.strdict[key] > 1:
            self.strdict[key] -= 1
            if key==self.max_str:
                self.max_count = 0
                self.max_str = ""
                for key, val in self.strdict.items():
                    if val > self.max_count:
                        self.max_str = key
                        self.max_count = val
            if self.strdict[key] < self.min_count:
                self.min_count = self.strdict[key]
                self.min_str = key
        else:
            del self.strdict[key]
            if key==self.max_str:
                self.max_count=0
                self.max_str=""
                for key,val in self.strdict.items():
                    if val > self.max_count:
                        self.max_str=key
                        self.max_count=val
            if key==self.min_str:
                self.min_count=5e4
                self.min_str=""
                for key,val in self.strdict.items():
                    if val<self.min_count:
                        self.min_str=key
                        self.min_count=val

    def getMaxKey(self) -> str:
        return self.max_str

    def getMinKey(self) -> str:
        return self.min_str

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
obj.inc("leet")
# obj.inc("d")
# obj.inc("a")
# obj.inc("b")
# obj.inc("c")
# obj.inc("d")
# obj.inc("c")
# obj.inc("d")
# obj.inc("d")
# obj.inc("a")
print(obj.getMaxKey())
print(obj.getMinKey())