#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/29
# project = leetcode535-TinyURL的加密解密-哈希表的简易实现
K1, K2 = 1117, 10 ** 9 + 7

class Codec:
    def __init__(self):
        self.dataBase = {}
        self.urlToKey = {}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlToKey:
            return "http://tinyurl.com/" + str(self.urlToKey[longUrl])
        key, base = 0, 1
        for c in longUrl:
            key = (key + ord(c) * base) % K2
            base = (base * K1) % K2
        while key in self.dataBase:
            key = (key + 1) % K2
        self.dataBase[key] = longUrl
        self.urlToKey[longUrl] = key
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        key = int(shortUrl[i + 1:])
        return self.dataBase[key]
