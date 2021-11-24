#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/24
# project = leetcode423
from collections import defaultdict, Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        mmap = defaultdict(int)
        dic = [{0: {'z': 1, 'e': 1, 'r': 1, 'o': 1}},
               {4: {'f': 1, 'o': 1, 'u': 1, 'r': 1}},
               {5: {'f': 1, 'i': 1, 'v': 1, 'e': 1}},
               {6: {'s': 1, 'i': 1, 'x': 1}},
               {8: {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}},
               {2: {'t': 1, 'w': 1, 'o': 1}},
               {3: {'t': 1, 'h': 1, 'r': 1, 'e': 2}},
               {7: {'s': 1, 'e': 2, 'v': 1, 'n': 1}},
               {1: {'o': 1, 'n': 1, 'e': 1}},
               {9: {'n': 2, 'i': 1, 'e': 1}}]

        for i in s:
            mmap[i] += 1
        ret = []
        for i in dic:
            flag = True
            while flag:
                for key, val in i[list(i.keys())[0]].items():
                    if mmap[key] < val:
                        flag = False
                        break
                if flag:
                    ret.append(chr(ord('0') + list(i.keys())[0]))
                    for key, val in i[list(i.keys())[0]].items():
                        mmap[key] -= val
        return ''.join(sorted(ret))

    def originalDigits2(self, s: str) -> str:
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]

        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))


solution = Solution()
s = "zeroonetwothreefourfivesixseveneightnine"
print(solution.originalDigits1(s))
# s=list(solution.originalDigits(s))
# print(''.join(sorted(s)))
